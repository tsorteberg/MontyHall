"""
Program: test_trial_generator.py
Author: Tom Sorteberg
Last date modified: 07/28/2020

The purpose of this program is to perform unit testing for the trial_generator
application.
"""
import unittest
from main import trial_generator


class MyTestCase(unittest.TestCase):

    def test01_validate_trials_blank(self):
        with self.assertRaises(NameError):
            self.assertEqual(False, trial_generator.validate_trials(""))

    def test02_validate_trials_set(self):
        with self.assertRaises(NameError):
            self.assertEqual(False, trial_generator.validate_trials("abc"))

    def test03_validate_trials_range_low(self):
        with self.assertRaises(NameError):
            self.assertEqual(False, trial_generator.validate_trials("-15"))

    def test04_validate_trials_range_high(self):
        with self.assertRaises(NameError):
            self.assertEqual(False, trial_generator.validate_trials("-15"))

    def test05_validate_filename_blank(self):
        with self.assertRaises(NameError):
            self.assertEqual(False, trial_generator.validate_filename(""))

    def test06_validate_filename_set(self):
        with self.assertRaises(NameError):
            self.assertEqual(False, trial_generator.validate_filename("!"))

    def test07_validate_filename_range(self):
        with self.assertRaises(NameError):
            self.assertEqual(False, trial_generator.validate_filename("Lorem ipsum "
                                                                      "dolor sit am"
                                                                      "et, consecte"
                                                                      "tur adipisci"
                                                                      "ng elit. Pra"
                                                                      "esent ac con"
                                                                      "gue nulla. I"
                                                                      "n diam augue"
                                                                      ", tristique "
                                                                      "non tincidun"
                                                                      "t sed, fauci"
                                                                      "bus vitae ni"
                                                                      "sl. Maecenas"
                                                                      " non nunc eu"
                                                                      " arcu tempor"
                                                                      " volutpat. I"
                                                                      "n molestie o"
                                                                      "dio ut males"
                                                                      "uada luctus. "
                                                                      "Nunc feugiat "
                                                                      "posuere bland"
                                                                      "it. Donec veh"
                                                                      ""))


if __name__ == '__main__':
    unittest.main()

#                      Test Case Coverage: Unit Test                          #
#          Input             Expected Output            Actual Output         #
#           ""                    False                     False             #
#          "abc"                  False                     False             #
#          -15                    False                     False             #
#          -15                    False                     False             #
#           ""                    False                     False             #
#           "!"                   False                     False             #
#       Lorem Ipsum               False                     False             #
