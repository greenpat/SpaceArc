import unittest
import Classes.Item


class test_Item(unittest.TestCase):
    def setUp(self):
        self.item1 = Classes.Item('Wrench', strength=1, tenacity=10)
        self.item2 = Classes.Item('Torch', speed=-2, tenacity=-2)

    def test_inherit(self):
        self.assertIsInstance(self.item1, Classes.Stats)

    def test_combine(self):
        self.item3 = Classes.Item(name='rocket', **Classes.Stats.combine(self.item1, self.item2).__dict__)
        self.assertEqual(self.item3.tenacity, 8)
        self.item4 = Classes.Stats.combine(self.item1, self.item3)
        self.assertEqual(self.item4.tenacity, 18)

    def test_name(self):
        self.assertEqual(self.item1.name, 'Wrench')

if __name__ == '__main__':
    unittest.main()