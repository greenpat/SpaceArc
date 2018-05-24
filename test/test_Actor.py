import unittest
import Classes
import Obj

class test_Actor(unittest.TestCase):

    def setUp(self):
        self.testman = Classes.Actor('Testronaut', intellect = 2, strength = 3)
        self.testman.items.append(Obj.items['Spiked Boots'])
        self.testman.items.append(Obj.items['Laptop'])
        self.testman.effects.append(Obj.effects['Resourceful'])
        self.testman.effects.append(Obj.effects['Password'])
        self.emptyman = Classes.Actor('Empty')


    def test_drop_temp(self):
        self.testman.drop_temp()
        self.assertTrue(Obj.items['Spiked Boots'] not in self.testman.items)
        self.assertTrue(Obj.items['Laptop'] in self.testman.items)
        self.assertTrue(Obj.effects['Password'] not in self.testman.effects)
        self.assertTrue(Obj.effects['Resourceful'] in self.testman.effects)

        try:
            self.emptyman.drop_temp()
        except:
            self.fail()