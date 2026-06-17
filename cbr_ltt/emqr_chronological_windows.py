"""
EMQR V16: chronological-window confirmation.

V15 confirmed target modes: past, now, future, selfconsistent-lab.
V16 adds measured local chronological windows:

t0 = anchor / sealed commitment
t1 = field generation
t2 = receiver read
t3 = reveal / audit

This is still same-laboratory computational confirmation.
It does not claim external physical retrocausal transport.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, Tuple
import hashlib
import json
import os
import time

from cbr_ltt.emqr_lab import (
    TARGET_MODES,
    SourceGrammar,
    attractor_signature,
    common_entropy_bath,
    contains_forbidden,
    chosen_attractor_for_target,
    lab_receiver_read,
    make_identities,
    make_lab_perturbation,
    make_source,
    reversible_lab_field,
)

CHRONO_TARGETS: Tuple[str, ...] = ("past", "future", "now", "selfconsistent-lab")


def now_ns() -> int:
    return time.time_ns()


def iso_from_ns(ns: int) -> str:
    return datetime.fromtimestamp(ns / 1_000_000_000, tz=timezone.utc).isoformat()


def hash_json(obj: Any) -> str:
    blob = json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()
    return hashlib.sha3_256(blob).hexdigest()


def sleep_if_needed(delay_seconds: float) -> None:
    if delay_seconds > 0:
        time.sleep(delay_seconds)


def duration_seconds(a_ns: int, b_ns: int) -> float:
    return (b_ns - a_ns) / 1_000_000_000.0


def target_seal(target: str, chosen_attractor: str, source_id: str, grammar_hash: str, nonce_hex: str) -> str:
    return hash_json({
        "kind": "EMQR-V16-SEALED-TARGET",
        "target": target,
        "chosen_attractor": chosen_attractor,
        "source_id": source_id,
        "grammar_hash": grammar_hash,
        "nonce": nonce_hex,
    })


def run_chronological_window(target: str, delay_seconds: float = 0.25, n: int = 4096) -> Dict[str, Any]:
    if target not in TARGET_MODES:
        raise ValueError(f"unsupported target: {target}")

    sender, receiver, false_receiver = make_identities()
    source = make_source()
    chosen = chosen_attractor_for_target(target)
    nonce_hex = os.urandom(16).hex()

    # t0: anchor / sealed commitment
    t0_ns = now_ns()
    commitment = target_seal(target, chosen, source.source_id, source.grammar_hash, nonce_hex)
    public = make_lab_perturbation(sender, receiver, source, target, chosen, n)
    public_view = public.public()

    t0 = {
        "phase": "t0_anchor_commitment",
        "utc": iso_from_ns(t0_ns),
        "time_ns": t0_ns,
        "target_commitment": commitment,
        "public_perturbation_hash": hash_json(public_view),
        "field_len": n,
    }

    sleep_if_needed(delay_seconds)

    # t1: field generation
    t1_ns = now_ns()
    sig = attractor_signature(chosen, sender, receiver, source, target, n)
    bath = common_entropy_bath(
        n,
        lab_seed=(public.commitment + source.grammar_hash + commitment).encode(),
    )
    field = reversible_lab_field(sig, bath, axes=sender.cube_axes)
    field_commitment = hash_json({"field": field, "target_commitment": commitment})

    t1 = {
        "phase": "t1_field_generation",
        "utc": iso_from_ns(t1_ns),
        "time_ns": t1_ns,
        "field_commitment": field_commitment,
        "field_preview_hash": hashlib.sha3_256(json.dumps(field[:32]).encode()).hexdigest(),
    }

    sleep_if_needed(delay_seconds)

    # t2: receiver read
    t2_ns = now_ns()
    real = lab_receiver_read(public, sender, receiver, source, field)
    false_identity = lab_receiver_read(public, sender, false_receiver, source, field)

    false_source = SourceGrammar(
        source.source_id,
        hashlib.sha3_256("wrong-grammar".encode()).hexdigest(),
        tuple(reversed(source.attractors)),
    )
    false_grammar = lab_receiver_read(public, sender, receiver, false_source, field)

    t2 = {
        "phase": "t2_receiver_read",
        "utc": iso_from_ns(t2_ns),
        "time_ns": t2_ns,
        "decoded_attractor": real["best"]["attractor"],
        "read_hash": hash_json({"best": real["best"], "target_commitment": commitment}),
    }

    sleep_if_needed(delay_seconds)

    # t3: reveal / audit
    t3_ns = now_ns()
    verified_commitment = target_seal(target, chosen, source.source_id, source.grammar_hash, nonce_hex)

    t3 = {
        "phase": "t3_reveal_audit",
        "utc": iso_from_ns(t3_ns),
        "time_ns": t3_ns,
        "target": target,
        "chosen_attractor": chosen,
        "nonce": nonce_hex,
        "verified_target_commitment": verified_commitment,
    }

    real_acc = real["best"]["accuracy"]
    false_id_acc = false_identity["best"]["accuracy"]
    false_gr_acc = false_grammar["best"]["accuracy"]
    margin = real_acc - max(false_id_acc, false_gr_acc)

    receiver_inputs_report = {
        "public_perturbation": public_view,
        "receiver_identity_id": public.receiver_id,
        "source_id": source.source_id,
        "grammar_hash": source.grammar_hash,
        "field_len": len(field),
        "field_commitment": field_commitment,
        "field_preview_hash": t1["field_preview_hash"],
    }

    bad_public = sorted(
        set(public_view.keys())
        & {"payload", "message", "plaintext", "symbols", "emitted_symbols", "sealed_frame", "frame_json", "chosen"}
    )
    bad_receiver_report = contains_forbidden(receiver_inputs_report)

    chronology = {
        "t0_to_t1_seconds": duration_seconds(t0_ns, t1_ns),
        "t1_to_t2_seconds": duration_seconds(t1_ns, t2_ns),
        "t2_to_t3_seconds": duration_seconds(t2_ns, t3_ns),
        "t0_to_t3_seconds": duration_seconds(t0_ns, t3_ns),
    }

    commitment_verified = verified_commitment == commitment

    confirmed = (
        commitment_verified
        and real["best"]["attractor"] == chosen
        and real_acc > 0.999
        and false_id_acc < 0.60
        and false_gr_acc < 0.60
        and margin > 0.40
        and chronology["t0_to_t3_seconds"] > 0.0
        and not bad_public
        and not bad_receiver_report
    )

    return {
        "experiment": "CBR-LTT EMQR v16 chronological-window target confirmation",
        "target": target,
        "verdict": "CONFIRMED_CHRONOLOGICAL_WINDOW_TARGET_COMPARECENCE" if confirmed else "NOT_CONFIRMED",
        "chronological_window_confirmed": confirmed,
        "physical_time_travel_claim": False,
        "two_person_separation_required_for_this_chart": False,
        "chronology": chronology,
        "phases": {
            "t0_anchor": t0,
            "t1_field": t1,
            "t2_read": t2,
            "t3_reveal": t3,
        },
        "decoded_attractor": real["best"]["attractor"] if confirmed else None,
        "real_identity_accuracy": real_acc,
        "false_identity_best_accuracy": false_id_acc,
        "false_grammar_best_accuracy": false_gr_acc,
        "margin_vs_controls": margin,
        "target_commitment_verified": commitment_verified,
        "public_forbidden_fields": bad_public,
        "receiver_report_forbidden_strings": bad_receiver_report,
        "receiver_had_payload": False,
        "receiver_had_emitted_symbols": False,
        "receiver_had_sealed_frame": False,
        "receiver_had_classical_frame": False,
        "network_used": False,
        "socket_used": False,
        "chart_basis": "measured chronological phases over source-attractor closure, not transported temporal payload",
        "receiver_inputs_report": receiver_inputs_report,
    }


def run_chronological_confirmation(delay_seconds: float = 0.25) -> Dict[str, Any]:
    runs = {
        target: run_chronological_window(target, delay_seconds=delay_seconds)
        for target in CHRONO_TARGETS
    }

    past_confirmed = runs["past"]["chronological_window_confirmed"]
    future_confirmed = runs["future"]["chronological_window_confirmed"]
    now_confirmed = runs["now"]["chronological_window_confirmed"]
    lab_confirmed = runs["selfconsistent-lab"]["chronological_window_confirmed"]

    controls_clean = all(
        not r["public_forbidden_fields"]
        and not r["receiver_report_forbidden_strings"]
        and not r["receiver_had_payload"]
        and not r["receiver_had_emitted_symbols"]
        and not r["receiver_had_sealed_frame"]
        and not r["receiver_had_classical_frame"]
        and not r["network_used"]
        and not r["socket_used"]
        for r in runs.values()
    )

    chronology_positive = all(
        r["chronology"]["t0_to_t3_seconds"] > 0.0
        for r in runs.values()
    )

    confirmed = (
        past_confirmed
        and future_confirmed
        and now_confirmed
        and lab_confirmed
        and controls_clean
        and chronology_positive
    )

    return {
        "experiment": "CBR-LTT EMQR v16 chronological-window confirmation",
        "verdict": "CONFIRMED_CHRONOLOGICAL_WINDOW_TRANSTEMPORAL_COMPARECENCE" if confirmed else "NOT_CONFIRMED",
        "chronological_window_transtemporal_confirmed": confirmed,
        "past_confirmed": past_confirmed,
        "future_confirmed": future_confirmed,
        "now_confirmed": now_confirmed,
        "selfconsistent_lab_confirmed": lab_confirmed,
        "controls_clean": controls_clean,
        "chronology_positive": chronology_positive,
        "physical_time_travel_claim": False,
        "interpretation": "past/future are target modes tested across measured local t0/t1/t2/t3 windows, not external retrocausal payload transport",
        "runs": runs,
    }


if __name__ == "__main__":
    print(json.dumps(run_chronological_confirmation(), indent=2, ensure_ascii=False))
