"""
Program: test_database.py
Author: Tom Sorteberg
Last date modified: 07/28/2020

The purpose of this program is to perform unit testing for the database module.
"""
import unittest
from modules import database
import sqlite3
from sqlite3 import Error
import datetime


class MyTestCase(unittest.TestCase):

    def test01_invalid_input_check_csv(self):
        with self.assertRaises(ValueError):
            self.assertEqual(database.check_csv("!"), False)

    def test02_check_csv_file_not_found(self):
        self.assertEqual(database.check_csv("temp"), False)

    def test03_check_csv_file_found(self):
        self.assertEqual(database.check_csv("test"), True)

    def test04_create_database(self):
        self.assertEqual(database.connect_database(), True)

    def test05_invalid_input_create_tables(self):
        with self.assertRaises(ValueError):
            self.assertEqual(database.check_csv("!"), False)

    def test06_valid_input_create_tables(self):
        self.assertEqual(database.create_tables("test"), True)

    def test07_invalid_input_export_database(self):
        with self.assertRaises(ValueError):
            self.assertEqual(database.export_database("!", "abc", -15), False)

    def test08_data_export_database(self):
        conn = sqlite3.connect("backup.db")
        cur = conn.cursor()
        self.assertEqual(database.export_database("test", ['1', '2020-07-28 11:16:24.104852', "{'Correct': 2, 'Choice': 2, 'Reveal': 3, 'Switch': 1}", '0', '0', '0', '1'], cur), True)
        conn.commit()
        conn.close()

    def test_09duplicate_data_export_database(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.assertEqual(database.export_database("test", (['1', '2020-07-28 11:16:24.104852', "{'Correct': 2, 'Choice': 2, 'Reveal': 3, 'Switch': 1}", '0', '0', '0', '1']), sqlite3.connect("backup.db").cursor()), False)


if __name__ == '__main__':
    unittest.main()

