"""
Program: test_monty.py
Author: Tom Sorteberg
Last date modified: 07/28/2020

The purpose of this program is to perform unit testing for the Monty class.
"""
import unittest
from definitions import monty
import datetime


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.monty = monty.Monty(10000)

    def tearDown(self):
        del self.monty

    def test_exception_constructor_invalid_type(self):
        with self.assertRaises(Exception):
            self.game = monty.Monty("abc")

    def test_exception_constructor_invalid_range(self):
        with self.assertRaises(Exception):
            self.game = monty.Monty(-15)

    def test_invalid_set_trials_type(self):
        with self.assertRaises(Exception):
            self.monty.set_trials("abc")

    def test_invalid_set_trials_range(self):
        with self.assertRaises(Exception):
            self.monty.set_trials(-15)

    def test_valid_get_trials(self):
        self.assertEqual(self.monty.get_trials(), 10000)

    def test_create_csv_file_exists(self):
        self.assertEqual(self.monty.create_csv("test"), False)

    def test_create_csv_invalid_filename(self):
        with self.assertRaises(ValueError):
            self.monty.create_csv("!")

    def test_invalid_input_run_trial(self):
        with self.assertRaises(ValueError):
            self.monty.run_trial("abc")

    def test_invalid_range_run_trial(self):
        with self.assertRaises(ValueError):
            self.monty.run_trial(-15)

    def test_valid_run_trial(self):
        self.assertIsInstance(self.monty.run_trial(1)[0], int)
        self.assertIsInstance(self.monty.run_trial(1)[1], datetime.datetime)
        self.assertIsInstance(self.monty.run_trial(1)[2], dict)
        self.assertIsInstance(self.monty.run_trial(1)[2].get("Correct"), int)
        self.assertIsInstance(self.monty.run_trial(1)[2].get("Choice"), int)
        self.assertIsInstance(self.monty.run_trial(1)[2].get("Reveal"), int)
        self.assertIsInstance(self.monty.run_trial(1)[2].get("Switch"), int)
        self.assertIsInstance(self.monty.run_trial(1)[3][0], int)
        self.assertIsInstance(self.monty.run_trial(1)[3][1], int)
        self.assertIsInstance(self.monty.run_trial(1)[3][2], int)
        self.assertIsInstance(self.monty.run_trial(1)[3][3], int)

    def test_invalid_input_export_csv(self):
        with self.assertRaises(ValueError):
            self.monty.export_csv("abc", "!")

    def test_valid_string(self):
        self.assertEqual(self.monty.__str__(), "Trials: 10000")

    def test_valid_repr(self):
        self.assertEqual(self.monty.__repr__(), "Monty(10000)")


if __name__ == '__main__':
    unittest.main()

#                      Test Case Coverage: Unit Test                          #
#          Input             Expected Output            Actual Output         #
#          "abc"                Exception                  Exception          #
#           -15                 Exception                  Exception          #
#          "abc"                Exception                  Exception          #
#           -15                 Exception                  Exception          #
#          10000                  10000                      10000            #
#          "test"                 False                      False            #
#           "!"                 ValueError                 ValueError         #
#          "abc"                ValueError                 ValueError         #
#           -15                 ValueError                 ValueError         #
#            1                     Pass                       Pass            #
#        "abc", "!"             ValueError                 ValueError         #
#           ()                    __str__                    __str__          #
#           ()                    __rpr__                    __rpr__          #
