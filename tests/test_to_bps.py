import unittest
from src.prb_calc import to_bps

class ToBPSTestCase(unittest.TestCase):
    def test_downlink_tdd_no_sym(self):
        self.assertEqual(to_bps(False, 28, 1, 50, symbol_format=1, is_tdd=True), 0.0)

    def test_uplink_tdd_no_sym(self):
        self.assertEqual(to_bps(True, 28, 1, 50, symbol_format=0, is_tdd=True), 0.0)

    def test_downlink_tdd_with_flex(self):
        self.assertEqual(to_bps(False, 28, 1, 50, symbol_format=15, is_tdd=True), 91489702.5)

    def test_downlink_tdd_no_flex(self):
        self.assertEqual(to_bps(False, 28, 1, 50, symbol_format=15, is_tdd=True, use_flex_sym=False), 0.0)

    def test_downlink_fdd_reserved_mcs(self):
        self.assertEqual(to_bps(False, 28, 1, 50, mcs_table=1, is_tdd=False), 0.0)

    def test_uplink_fdd_mismatch_bw_and_numerology(self):
        self.assertEqual(to_bps(True, 28, 2, 3, is_tdd=False), 0.0)

    def test_downlink_fdd(self):
        self.assertEqual(to_bps(False, 28, 1, 50, is_tdd=False), 213475972.5)

    def test_uplink_fdd(self):
        self.assertEqual(to_bps(True, 28, 1, 50, is_tdd=False), 228369645.0)
