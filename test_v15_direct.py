import json
from cbr_ltt.emqr_lab import run_lab_confirmation, run_transtemporal_confirmation

past = run_lab_confirmation("past")
future = run_lab_confirmation("future")
batch = run_transtemporal_confirmation()

assert past["verdict"] == "CONFIRMED_TARGET_SOURCE_ATTRACTOR_COMPARECENCE"
assert past["target_mode_confirmed"] is True
assert past["decoded_attractor"] == "PAST SELFCONSISTENT"
assert past["real_identity_accuracy"] > 0.999
assert past["false_identity_best_accuracy"] < 0.60
assert past["false_grammar_best_accuracy"] < 0.60
assert past["margin_vs_controls"] > 0.40
assert past["receiver_had_payload"] is False
assert past["receiver_had_emitted_symbols"] is False
assert past["receiver_had_sealed_frame"] is False
assert past["network_used"] is False
assert past["socket_used"] is False

assert future["verdict"] == "CONFIRMED_TARGET_SOURCE_ATTRACTOR_COMPARECENCE"
assert future["target_mode_confirmed"] is True
assert future["decoded_attractor"] == "FUTURE SELFCONSISTENT"
assert future["real_identity_accuracy"] > 0.999
assert future["false_identity_best_accuracy"] < 0.60
assert future["false_grammar_best_accuracy"] < 0.60
assert future["margin_vs_controls"] > 0.40
assert future["receiver_had_payload"] is False
assert future["receiver_had_emitted_symbols"] is False
assert future["receiver_had_sealed_frame"] is False
assert future["network_used"] is False
assert future["socket_used"] is False

assert batch["verdict"] == "CONFIRMED_TRANSTEMPORAL_TARGET_COMPARECENCE"
assert batch["transtemporal_target_modes_confirmed"] is True
assert batch["past_confirmed"] is True
assert batch["now_confirmed"] is True
assert batch["future_confirmed"] is True
assert batch["selfconsistent_lab_confirmed"] is True
assert batch["controls_clean"] is True

print(json.dumps({
    "direct_test": "PASSED",
    "batch_verdict": batch["verdict"],
    "past_confirmed": batch["past_confirmed"],
    "future_confirmed": batch["future_confirmed"],
    "controls_clean": batch["controls_clean"]
}, indent=2, ensure_ascii=False))
