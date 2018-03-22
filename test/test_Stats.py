import unittest
from Classes.Stats import Stats


class test_Stats(unittest.TestCase):
    def setUp(self):
        self.stats1 = Stats(strength=2, speed=8, intellect=12, tenacity=1)
        self.stats2 = Stats(strength=0, speed=10, intellect=-2, tenacity=1)
        self.stats3 = Stats()

    def test_combine(self):
        combined = Stats.combine(self.stats1, self.stats2)
        self.assertEqual(combined.strength, 2)
        self.assertEqual(combined.speed, 18)
        self.assertEqual(combined.intellect, 10)
        self.assertEqual(combined.tenacity, 2)

    def test_multiply(self):
        Stats.multiply(self.stats2, 2)
        self.assertEqual(self.stats2.strength, 0)
        self.assertEqual(self.stats2.speed, 20)
        self.assertEqual(self.stats2.intellect, -4)
        self.assertEqual(self.stats2.tenacity, 2)
        Stats.multiply(self.stats2, .5)
        self.assertEqual(self.stats2.strength, 0)
        self.assertEqual(self.stats2.speed, 10)
        self.assertEqual(self.stats2.intellect, -2)
        self.assertEqual(self.stats2.tenacity, 1)

    def test_reset(self):
        self.stats3.reset(100)
        for _ in Stats.attribs:
            self.assertTrue(getattr(self.stats3, _) == 100)

    def tearDown(self):
        del (self)


if __name__ == '__main__':
    unittest.main()
