import unittest
from src.prb_calc import to_prb

class ToBPSTestCase(unittest.TestCase):
    def test_downlink_tdd_no_sym(self):
        self.assertEqual(to_prb(8678678.0, False, 28, 1, 50, symbol_format=1, is_tdd=True), 0)

    def test_uplink_tdd_no_sym(self):
        self.assertEqual(to_prb(345345.0, True, 28, 1, 50, symbol_format=0, is_tdd=True), 0)

    def test_downlink_tdd_with_flex(self):
        self.assertEqual(to_prb(91489702.5, False, 28, 1, 50, symbol_format=15, is_tdd=True), 100)

    def test_downlink_tdd_with_flex_half(self):
        self.assertEqual(to_prb(45744851.25, False, 28, 1, 50, symbol_format=15, is_tdd=True), 50)

    def test_downlink_tdd_with_flex_zero(self):
        self.assertEqual(to_prb(0, False, 28, 1, 50, symbol_format=15, is_tdd=True), 0)

    def test_downlink_fdd(self):
        self.assertEqual(to_prb(213475972.5, False, 28, 1, 50, is_tdd=False), 100)

    def test_uplink_fdd(self):
        self.assertEqual(to_prb(228369645.0, True, 28, 1, 50, is_tdd=False), 100)
