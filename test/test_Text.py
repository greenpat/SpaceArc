import unittest
import Text

class test_Text(unittest.TestCase):

    def setUp(self):
        messy1 = '''
        Indented  doublespace
        '''
        self.assertEqual(satext(messy1),"Indented doublespace")
        messy2 = """ A long story:
        
        
        One day there were too many newlines
        
        
        and then suddenly
        
a misplaced align
             the end.
        """
        messy3 = """
        This is just a  tab     in the middle of    the sentence. Nothing
        we can't                    take care of.
        """