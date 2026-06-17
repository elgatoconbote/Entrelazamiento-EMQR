import unittest
from cbr_ltt.emqr_lab import run_lab_confirmation


class TestLabConfirmation(unittest.TestCase):
    def test_same_lab_source_attractor_confirmed(self):
        r = run_lab_confirmation("selfconsistent-lab")
        self.assertIn(
            r["verdict"],
            [
                "CONFIRMED_SAME_LAB_SOURCE_ATTRACTOR_COMPARECENCE",
                "CONFIRMED_TARGET_SOURCE_ATTRACTOR_COMPARECENCE",
            ],
        )
        self.assertTrue(
            r.get("same_laboratory_conditions_confirmed")
            or r.get("target_mode_confirmed")
        )
        self.assertEqual(r["decoded_attractor"], "EMQR LAB COMPARECENCE OK")
        self.assertGreater(r["real_identity_accuracy"], 0.999)
        self.assertLess(r["false_identity_best_accuracy"], 0.60)
        self.assertLess(r["false_grammar_best_accuracy"], 0.60)
        self.assertGreater(r["margin_vs_controls"], 0.40)
        self.assertEqual(r["public_forbidden_fields"], [])
        self.assertEqual(r["receiver_report_forbidden_strings"], [])
        self.assertFalse(r["receiver_had_payload"])
        self.assertFalse(r["receiver_had_emitted_symbols"])
        self.assertFalse(r["receiver_had_sealed_frame"])
        self.assertFalse(r["network_used"])
        self.assertFalse(r["socket_used"])


if __name__ == "__main__":
    unittest.main()
