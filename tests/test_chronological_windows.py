import unittest
from cbr_ltt.emqr_chronological_windows import run_chronological_confirmation


class TestChronologicalWindows(unittest.TestCase):
    def test_v16_chronological_windows_confirmed(self):
        r = run_chronological_confirmation(delay_seconds=0.01)
        self.assertEqual(
            r["verdict"],
            "CONFIRMED_CHRONOLOGICAL_WINDOW_TRANSTEMPORAL_COMPARECENCE",
        )
        self.assertTrue(r["chronological_window_transtemporal_confirmed"])
        self.assertTrue(r["past_confirmed"])
        self.assertTrue(r["future_confirmed"])
        self.assertTrue(r["now_confirmed"])
        self.assertTrue(r["selfconsistent_lab_confirmed"])
        self.assertTrue(r["controls_clean"])
        self.assertTrue(r["chronology_positive"])

        past = r["runs"]["past"]
        future = r["runs"]["future"]

        self.assertEqual(past["decoded_attractor"], "PAST SELFCONSISTENT")
        self.assertEqual(future["decoded_attractor"], "FUTURE SELFCONSISTENT")

        self.assertGreater(past["chronology"]["t0_to_t3_seconds"], 0.0)
        self.assertGreater(future["chronology"]["t0_to_t3_seconds"], 0.0)

        self.assertFalse(past["receiver_had_payload"])
        self.assertFalse(future["receiver_had_payload"])
        self.assertFalse(past["network_used"])
        self.assertFalse(future["network_used"])


if __name__ == "__main__":
    unittest.main()
