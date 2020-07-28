"""
Program: test_pyplot.py
Author: Tom Sorteberg
Last date modified: 07/28/2020

The purpose of this program is to perform unit testing for the pyplot module.
"""

import unittest
from modules import pyplot


class MyTestCase(unittest.TestCase):

    def test_pyplot_file_not_found(self):
        self.assertEqual(pyplot.pyplot("notfound"), False)

    def test_pyplot_invalid_input(self):
        with self.assertRaises(ValueError):
            self.assertEqual(pyplot.pyplot("!"), False)


if __name__ == '__main__':
    unittest.main()

#                      Test Case Coverage: Unit Test                          #
#          Input             Expected Output            Actual Output         #
#        "notfound"               False                     False             #
#           "!"                   False                     False             #

