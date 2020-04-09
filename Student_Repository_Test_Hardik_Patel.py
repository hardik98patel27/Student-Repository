from typing import Dict,List
import unittest

from Student_Repository_Hardik_Patel import Repository

class TestAll(unittest.TestCase):
    """Helps to test all the functions"""
    def test_data_for_pretty1(self):
        """This function is used to test prettyprint_1 function's data"""
        R1: Repository = Repository("/Users/Hardik/Downloads/SSW 810/Assign 9")
        expected:Dict={'10103': ('Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']), '10115': ('Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']), '10172': ('Forbes, I', ['SSW 555', 'SSW 567']), '10175': ('Erickson, D', ['SSW 564', 'SSW 567', 'SSW 687']), '10183': ('Chapman, O', ['SSW 689']), '11399': ('Cordova, I', ['SSW 540']), '11461': ('Wright, U', ['SYS 611', 'SYS 750', 'SYS 800']), '11658': ('Kelly, P', ['SSW 540']), '11714': ('Morton, A', ['SYS 611', 'SYS 645']), '11788': ('Fuller, E', ['SSW 540'])}

        expected1:Dict={'10103': ('Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']), '10115': ('Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']), '10172': ('Forbes, I', ['SSW 555', 'SSW 567']), '10175': ('Erickson, D', ['SSW 564', 'SSW 567', 'SSW 687']), '10183': ('Chapman, O', ['SSW 689']), '11399': ('Cordova, I', ['SSW 540']), '11461': ('Wright, U', ['SYS 611', 'SYS 750', 'SYS 800']), '11658': ('Kelly, P', ['SSW 540']), '11714': ('Morton, A', ['SYS 611', 'SYS 645']), '11788': ('Fuller, E', ['SSW 504'])}

        self.assertEqual(R1.printpretty_1(),expected)
        self.assertNotEqual(R1.printpretty_1(), expected1)


    def test_data_for_pretty2(self):
        """This function is used to test prettyprint_2 function's data"""
        R2: Repository = Repository("/Users/Hardik/Downloads/SSW 810/Assign 9")
        expected3:Dict={'98765': ('Einstein, A', 'SFEN', 'SSW 540', 3), '98764': ('Feynman, R', 'SFEN', 'CS 545', 1), '98763': ('Newton, I', 'SFEN', 'SSW 689', 1), '98760': ('Darwin, C', 'SYEN', 'SYS 645', 1)}


        expected4:Dict={'98765': ('Einstein, A', 'SFEN', 'SSW 540', 3), '98764': ('Feynman, R', 'SFEN', 'CS 545', 1), '98763': ('Newton, I', 'SFEN', 'SSW 689', 1), '98760': ('Darwin, C', 'SYEN', 'SYS 645', 4)}


        self.assertEqual(R2.printpretty_2(),expected3)
        self.assertNotEqual(R2.printpretty_2(), expected4)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
