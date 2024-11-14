import unittest
from src.prb_calc import latency

class LatencyTestCase(unittest.TestCase):
    def test_latency_n0(self):
        self.assertEqual(latency(0), 1.0)
    def test_latency_n1(self):
        self.assertEqual(latency(1), 0.5)
    def test_latency_n2(self):
        self.assertEqual(latency(2), 0.25)
    def test_latency_n3(self):
        self.assertEqual(latency(3), 0.125)
