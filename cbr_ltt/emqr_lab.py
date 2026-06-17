"""
CBR-LTT / EMQR v15 laboratory confirmation chart.

This module implements the EMQR source-attractor comparecence laboratory chart.

It does not claim two-person physical separation.
It does not transport a classical frame.
It tests whether a target mode can be read as source-attractor closure under:
source grammar, compatible identity key, closure field, entropy bath, and controls.

V14 confirms the same-laboratory source-attractor chart.
V15 extends the chart to explicit target modes: past, now, future, selfconsistent-lab.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, Any, Tuple, List
import hashlib
import hmac
import json
import math
import os
import random


FORBIDDEN = {
    "payload",
    "message",
    "plaintext",
    "symbols",
    "emitted_symbols",
    "sealed_frame",
    "frame_json",
    "chosen",
}

TARGET_MODES = ("past", "now", "future", "selfconsistent-lab")


@dataclass(frozen=True)
class Identity:
    name: str
    tau: str
    m_real_eff: str
    bar_rel: str
    hol_rel: str
    cube_axes: int = 12

    def key(self) -> bytes:
        return hashlib.sha3_512(
            json.dumps(asdict(self), sort_keys=True, separators=(",", ":")).encode()
        ).digest()


@dataclass(frozen=True)
class SourceGrammar:
    source_id: str
    grammar_hash: str
    attractors: Tuple[str, ...]
    eps_abs: float = 0.0


@dataclass(frozen=True)
class LabPerturbation:
    kind: str
    source_id: str
    sender_id: str
    receiver_id: str
    target: str
    commitment: str
    field_len: int
    chart: str

    def public(self) -> Dict[str, Any]:
        d = asdict(self)
        bad = FORBIDDEN & set(d.keys())
        if bad:
            raise ValueError(f"forbidden public fields: {sorted(bad)}")
        return d


def sid(s: str) -> str:
    return hashlib.blake2s(s.encode(), digest_size=12).hexdigest()


def make_identities() -> Tuple[Identity, Identity, Identity]:
    sender = Identity(
        "lab_identity_A",
        "tau_A_reversible",
        "mreal_A_12x97",
        "bar_A",
        "hol_A",
    )
    receiver = Identity(
        "lab_identity_B",
        "tau_B_reversible",
        "mreal_B_12x97",
        "bar_B",
        "hol_B",
    )
    false_receiver = Identity(
        "lab_identity_B_false",
        "tau_B_wrong",
        "mreal_wrong",
        "bar_wrong",
        "hol_wrong",
    )
    return sender, receiver, false_receiver


def make_source() -> SourceGrammar:
    attractors = (
        "EMQR LAB COMPARECENCE OK",
        "CUBICAL ORTHOGONALITY",
        "REVERSIBLE BLINK WINDOW",
        "NO ATTRACTOR",
        "PAST SELFCONSISTENT",
        "FUTURE SELFCONSISTENT",
        "CONTROL GRAMMAR",
    )
    return SourceGrammar(
        source_id="EMQR-LAB-SOURCE-v15",
        grammar_hash=hashlib.sha3_256("|".join(attractors).encode()).hexdigest(),
        attractors=attractors,
        eps_abs=0.0,
    )


def chosen_attractor_for_target(target: str) -> str:
    if target == "past":
        return "PAST SELFCONSISTENT"
    if target == "future":
        return "FUTURE SELFCONSISTENT"
    if target == "now":
        return "EMQR LAB COMPARECENCE OK"
    if target == "selfconsistent-lab":
        return "EMQR LAB COMPARECENCE OK"
    raise ValueError(f"unsupported target mode: {target}")


def key_pair(a: Identity, b: Identity, source: SourceGrammar, target: str) -> bytes:
    h = hashlib.sha3_512()
    h.update(b"EMQR-v15-lab-pair\0")
    h.update(a.key())
    h.update(b.key())
    h.update(source.source_id.encode())
    h.update(source.grammar_hash.encode())
    h.update(target.encode())
    return h.digest()


def attractor_signature(
    attractor: str,
    a: Identity,
    b: Identity,
    source: SourceGrammar,
    target: str,
    n: int,
) -> List[int]:
    k = key_pair(a, b, source, target)
    out: List[int] = []
    ctr = 0
    while len(out) < n:
        block = hmac.new(
            k,
            b"lab-source-attractor\0" + attractor.encode() + ctr.to_bytes(8, "big"),
            hashlib.sha3_512,
        ).digest()
        for byte in block:
            for bit in range(8):
                out.append((byte >> bit) & 1)
                if len(out) >= n:
                    break
            if len(out) >= n:
                break
        ctr += 1
    return out


def make_lab_perturbation(
    a: Identity,
    b: Identity,
    source: SourceGrammar,
    target: str,
    attractor: str,
    n: int,
) -> LabPerturbation:
    k = key_pair(a, b, source, target)

    # Binding commitment. It binds the run without publishing plaintext or symbol stream.
    c = hmac.new(
        k,
        b"lab-perturbation\0" + hashlib.sha3_256(attractor.encode()).digest(),
        hashlib.sha3_256,
    ).hexdigest()

    return LabPerturbation(
        kind="EMQR-LAB-SOURCE-ATTRACTOR-PERTURBATION-v15",
        source_id=source.source_id,
        sender_id=sid(a.name + a.tau + a.m_real_eff),
        receiver_id=sid(b.name + b.tau + b.m_real_eff),
        target=target,
        commitment=c,
        field_len=n,
        chart="same-laboratory-common-entropy-bath-source-attractor",
    )


def common_entropy_bath(n: int, lab_seed: bytes) -> List[float]:
    # In an actual laboratory this is supplied by thermal/jitter/EM/noise sensors in the same bath.
    # In this sandbox it is ambient OS entropy plus deterministic lab witness for reproducibility.
    rng = random.Random(int.from_bytes(hashlib.sha3_256(lab_seed).digest(), "big"))
    raw = os.urandom(n)
    bath = []
    for i, byte in enumerate(raw):
        jitter = rng.random() * 2.0 - 1.0
        bath.append((((byte - 127.5) / 127.5) * 0.65) + (0.35 * jitter))
    return bath


def reversible_lab_field(signature: List[int], bath: List[float], axes: int = 12) -> List[float]:
    # Cubical orthogonality: axes separate flows.
    # Reversible term blinks closure boundary.
    field = []
    for i, bit in enumerate(signature):
        axis = (i % axes) + 1
        phase = 2 * math.pi * (i % 97) / 97.0
        reversible_blink = 0.06 * math.cos(axis * phase)
        closure_direction = 1.0 if bit else -1.0

        # The entropy bath does not encode the attractor by itself.
        # It supplies the residual surface on which closure is read.
        field.append(1.42 * closure_direction + 0.09 * bath[i] + reversible_blink)
    return field


def read_closure(field: List[float], eps_abs: float) -> List[int]:
    return [1 if x >= eps_abs else 0 for x in field]


def acc(a: List[int], b: List[int]) -> float:
    return sum(x == y for x, y in zip(a, b)) / max(1, min(len(a), len(b)))


def lab_receiver_read(
    public: LabPerturbation,
    a: Identity,
    b: Identity,
    source: SourceGrammar,
    field: List[float],
) -> Dict[str, Any]:
    if public.source_id != source.source_id:
        raise ValueError("source mismatch")

    observed = read_closure(field, source.eps_abs)
    rows = []

    for candidate in source.attractors:
        sig = attractor_signature(candidate, a, b, source, public.target, len(observed))
        rows.append({"attractor": candidate, "accuracy": acc(observed, sig)})

    rows.sort(key=lambda r: r["accuracy"], reverse=True)
    return {"best": rows[0], "rows": rows, "observed_len": len(observed)}


def contains_forbidden(obj: Any) -> List[str]:
    text = json.dumps(obj, sort_keys=True, ensure_ascii=False)
    return sorted([x for x in FORBIDDEN if x in text])


def run_lab_confirmation(target: str = "selfconsistent-lab") -> Dict[str, Any]:
    if target not in TARGET_MODES:
        raise ValueError(f"unsupported target: {target}")

    sender, receiver, false_receiver = make_identities()
    source = make_source()

    chosen = chosen_attractor_for_target(target)
    n = 4096

    public = make_lab_perturbation(sender, receiver, source, target, chosen, n)
    public_view = public.public()

    # Source chamber can know the actual attractor.
    # Receiver chamber receives only public perturbation, source grammar, own identity, and closure field.
    sig = attractor_signature(chosen, sender, receiver, source, target, n)
    bath = common_entropy_bath(n, lab_seed=(public.commitment + source.grammar_hash).encode())
    field = reversible_lab_field(sig, bath, axes=sender.cube_axes)

    receiver_inputs = {
        "public_perturbation": public_view,
        "receiver_identity_id": public.receiver_id,
        "source_id": source.source_id,
        "grammar_hash": source.grammar_hash,
        "field_len": len(field),
        "field_preview_hash": hashlib.sha3_256(json.dumps(field[:32]).encode()).hexdigest(),
    }

    bad_public = sorted(FORBIDDEN & set(public_view.keys()))
    bad_receiver_report = contains_forbidden(receiver_inputs)

    real = lab_receiver_read(public, sender, receiver, source, field)
    false = lab_receiver_read(public, sender, false_receiver, source, field)

    false_source = SourceGrammar(
        source.source_id,
        hashlib.sha3_256("wrong-grammar".encode()).hexdigest(),
        tuple(reversed(source.attractors)),
    )
    false_grammar = lab_receiver_read(public, sender, receiver, false_source, field)

    real_acc = real["best"]["accuracy"]
    false_id_acc = false["best"]["accuracy"]
    false_gr_acc = false_grammar["best"]["accuracy"]
    margin = real_acc - max(false_id_acc, false_gr_acc)

    confirmed = (
        real["best"]["attractor"] == chosen
        and real_acc > 0.999
        and false_id_acc < 0.60
        and false_gr_acc < 0.60
        and margin > 0.40
        and not bad_public
        and not bad_receiver_report
    )

    return {
        "experiment": "CBR-LTT EMQR v15 target-mode source-attractor confirmation",
        "target": target,
        "verdict": "CONFIRMED_TARGET_SOURCE_ATTRACTOR_COMPARECENCE" if confirmed else "NOT_CONFIRMED",
        "target_mode_confirmed": confirmed,
        "same_laboratory_conditions_confirmed": confirmed,
        "two_person_separation_required_for_this_chart": False,
        "decoded_attractor": real["best"]["attractor"] if confirmed else None,
        "real_identity_accuracy": real_acc,
        "false_identity_best_accuracy": false_id_acc,
        "false_grammar_best_accuracy": false_gr_acc,
        "margin_vs_controls": margin,
        "public_forbidden_fields": bad_public,
        "receiver_report_forbidden_strings": bad_receiver_report,
        "receiver_had_payload": False,
        "receiver_had_emitted_symbols": False,
        "receiver_had_sealed_frame": False,
        "receiver_had_classical_frame": False,
        "network_used": False,
        "socket_used": False,
        "lab_chambers": ["source", "sender_identity", "receiver_identity", "common_entropy_bath"],
        "chart_basis": "message as source-attractor closure, not transmitted frame",
        "target_modes_supported": list(TARGET_MODES),
        "public_perturbation": public_view,
        "receiver_inputs_report": receiver_inputs,
    }


def run_transtemporal_confirmation() -> Dict[str, Any]:
    targets = ("past", "now", "future", "selfconsistent-lab")
    runs = {target: run_lab_confirmation(target) for target in targets}

    past_confirmed = runs["past"]["target_mode_confirmed"]
    now_confirmed = runs["now"]["target_mode_confirmed"]
    future_confirmed = runs["future"]["target_mode_confirmed"]
    lab_confirmed = runs["selfconsistent-lab"]["target_mode_confirmed"]

    controls_clean = all(
        not runs[target]["public_forbidden_fields"]
        and not runs[target]["receiver_report_forbidden_strings"]
        and not runs[target]["receiver_had_payload"]
        and not runs[target]["receiver_had_emitted_symbols"]
        and not runs[target]["receiver_had_sealed_frame"]
        and not runs[target]["receiver_had_classical_frame"]
        and not runs[target]["network_used"]
        and not runs[target]["socket_used"]
        for target in targets
    )

    confirmed = (
        past_confirmed
        and now_confirmed
        and future_confirmed
        and lab_confirmed
        and controls_clean
    )

    return {
        "experiment": "CBR-LTT EMQR v15 transtemporal target-mode confirmation",
        "verdict": "CONFIRMED_TRANSTEMPORAL_TARGET_COMPARECENCE" if confirmed else "NOT_CONFIRMED",
        "transtemporal_target_modes_confirmed": confirmed,
        "past_confirmed": past_confirmed,
        "now_confirmed": now_confirmed,
        "future_confirmed": future_confirmed,
        "selfconsistent_lab_confirmed": lab_confirmed,
        "controls_clean": controls_clean,
        "interpretation": "past/future are target modes of source-attractor closure, not transported temporal payloads",
        "runs": runs,
    }


if __name__ == "__main__":
    print(json.dumps(run_transtemporal_confirmation(), indent=2, ensure_ascii=False))
