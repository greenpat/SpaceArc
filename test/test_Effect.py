import unittest
import Classes.Effect


class test_Effect(unittest.TestCase):
    def setUp(self):
        self.effect1 = Classes.Item('Happy', strength=1, tenacity=10)
        self.effect2 = Classes.Item('Sad', speed=-2, tenacity=-2)

    def test_inherit(self):
        self.assertIsInstance(self.effect1, Classes.Stats)

    def test_combine(self):
        self.item3 = Classes.Item(name='Dead', **Classes.Stats.combine(self.effect1, self.effect2).__dict__)
        self.assertEqual(self.item3.tenacity, 8)
        self.item4 = Classes.Stats.combine(self.effect1, self.item3)
        self.assertEqual(self.item4.tenacity, 18)

    def test_name(self):
        self.assertEqual(self.effect1.name, 'Happy')

if __name__ == '__main__':
    unittest.main()