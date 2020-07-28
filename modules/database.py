"""
Program: monty.py
Author: Tom Sorteberg
Last date modified: 07/28/2020

The purpose of this module is to provide a means to backup collected
trial data to an SqlLite database.  The input is provided by the calling
function; the functions return a boolean value.
"""
from constants import constants
import sqlite3
from sqlite3 import Error


def check_csv(filename):
    """
    Function to check if csv file for backup exists.
    :param filename: Required: str.
    :return: Returns a bool.
    """
    # Define set for input validation.
    character_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01"
                        "23456789 ")
    # Input validation.
    if not (character_set.issuperset(filename)
            and (constants.LOW <= len(filename) <= constants.LENGTH)):
        # Raises ValueError.
        raise ValueError
    else:
        # Set return variable bool under fail assumption.
        _success = False
        try:
            open(filename + ".csv", 'r')
        except FileNotFoundError:
            # Bypass exception to continue program execution.
            pass
        else:
            # If csv file is located, return True.
            _success = True
        # If file not found, return default value.
        return _success


def connect_database():
    """
    Function to create database connection.
    :return: Returns a bool.
    """
    # Set return variable bool under fail assumption.
    _success = False
    # Attempt to connect to database.
    try:
        sqlite3.connect("backup.db")
    except Error:
        # Bypass exception to continue program execution.
        pass
    else:
        # If database connection successful, return True.
        _success = True
    # If database connection fails, return default value.
    return _success


def create_tables(filename):
    """
    Function to create a table of member filename.
    :param filename: Required: str.
    :return: Returns a bool
    """
    # Define set for input validation.
    character_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01"
                        "23456789 ")
    # Input Validation.
    if not (character_set.issuperset(filename)
            and (constants.LOW <= len(filename) <= constants.LENGTH)):
        # Raises ValueError
        raise ValueError
    else:
        # Initiate connection to database and define cursor.
        conn = sqlite3.connect("backup.db")
        cur = conn.cursor()

        # Variable declaration for sql statements.
        sql_table = ("CREATE TABLE IF NOT EXISTS " + "'" + filename + "'"
                     + "(id text PRIMARY KEY,"
                       " time text NOT NULL,"
                       " results text NOT NULL,"
                       " correctNoSwitch text NOT NULL, "
                       " correctSwitch text NOT NULL, "
                       " incorrectNoSwitch text NOT NULL,"
                       " incorrectSwitch text NOT NULL);")
        # Set return variable bool under fail assumption.
        _success = False
        # Attempt to create table.
        if conn is not None:
            try:
                cur.execute(sql_table)
            except Error:
                # Bypass exception to continue program execution.
                pass
            else:
                # If table creation is successful, return True.
                _success = True
        else:
            # If table creation fails, return default value.
            return _success
        # If table creation fails, return default value.
        return _success


def export_database(filename, row, cur):
    """
    Function to export a single row from csv file as a new record.
    :param filename: Required: str.
    :param row: Required: list.
    :param cur: Required: cursor object.
    :return: Returns a bool.
    """
    # Define set for input validation.
    character_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01"
                        "23456789 ")
    # Input Validation.
    if not (character_set.issuperset(filename)
            and (constants.LOW <= len(filename) <= constants.LENGTH)) \
            or not isinstance(row, list) or not isinstance(cur, sqlite3.Cursor):
        # Raises ValueError
        raise ValueError
    else:
        # Set return variable bool under fail assumption.
        _success = False
        # Attempt to import line from csv file into database.
        try:
            to_db = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            # print(to_db)
            cur.execute(
                "INSERT INTO " +
                "'" + filename +
                "'" + "(id, time, results, correctNoSwitch, correctSwitch, "
                      "incorrectNoSwitch, incorrectSwitch) "
                      "VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)
        except sqlite3.IntegrityError:
            # Raises IntegrityError.
            raise sqlite3.IntegrityError
        else:
            # If import is successful, return True.
            _success = True
        # If import fails, return default value.
        return _success
