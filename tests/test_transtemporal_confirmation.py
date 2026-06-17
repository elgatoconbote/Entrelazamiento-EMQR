import unittest
from cbr_ltt.emqr_lab import run_lab_confirmation, run_transtemporal_confirmation


class TestTranstemporalConfirmation(unittest.TestCase):
    def test_past_target_confirmed(self):
        r = run_lab_confirmation("past")
        self.assertEqual(r["verdict"], "CONFIRMED_TARGET_SOURCE_ATTRACTOR_COMPARECENCE")
        self.assertTrue(r["target_mode_confirmed"])
        self.assertEqual(r["decoded_attractor"], "PAST SELFCONSISTENT")
        self.assertGreater(r["real_identity_accuracy"], 0.999)
        self.assertLess(r["false_identity_best_accuracy"], 0.60)
        self.assertLess(r["false_grammar_best_accuracy"], 0.60)
        self.assertGreater(r["margin_vs_controls"], 0.40)
        self.assertFalse(r["receiver_had_payload"])
        self.assertFalse(r["receiver_had_emitted_symbols"])
        self.assertFalse(r["receiver_had_sealed_frame"])
        self.assertFalse(r["network_used"])
        self.assertFalse(r["socket_used"])

    def test_future_target_confirmed(self):
        r = run_lab_confirmation("future")
        self.assertEqual(r["verdict"], "CONFIRMED_TARGET_SOURCE_ATTRACTOR_COMPARECENCE")
        self.assertTrue(r["target_mode_confirmed"])
        self.assertEqual(r["decoded_attractor"], "FUTURE SELFCONSISTENT")
        self.assertGreater(r["real_identity_accuracy"], 0.999)
        self.assertLess(r["false_identity_best_accuracy"], 0.60)
        self.assertLess(r["false_grammar_best_accuracy"], 0.60)
        self.assertGreater(r["margin_vs_controls"], 0.40)
        self.assertFalse(r["receiver_had_payload"])
        self.assertFalse(r["receiver_had_emitted_symbols"])
        self.assertFalse(r["receiver_had_sealed_frame"])
        self.assertFalse(r["network_used"])
        self.assertFalse(r["socket_used"])

    def test_transtemporal_batch_confirmed(self):
        r = run_transtemporal_confirmation()
        self.assertEqual(r["verdict"], "CONFIRMED_TRANSTEMPORAL_TARGET_COMPARECENCE")
        self.assertTrue(r["transtemporal_target_modes_confirmed"])
        self.assertTrue(r["past_confirmed"])
        self.assertTrue(r["now_confirmed"])
        self.assertTrue(r["future_confirmed"])
        self.assertTrue(r["selfconsistent_lab_confirmed"])
        self.assertTrue(r["controls_clean"])


if __name__ == "__main__":
    unittest.main()
