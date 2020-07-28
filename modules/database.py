"""
Program: monty.py
Author: Tom Sorteberg
Last date modified: 07/28/2020

The purpose of this module is to provide a means to backup collected
trial data to an SqlLite database.  The input is provided by the calling
function; the functions return a boolean value.
"""

def check_csv(filename):
    """
    Function to check if csv file for backup exists.
    :param filename: Required: str.
    :return: Returns a bool.
    """
    pass

def connect_database():
    """
    Function to create database connection.
    :return: Returns a bool.
    """
    pass

def create_tables(filename):
    """
    Function to create a table of member filename.
    :param filename: Required: str.
    :return: Returns a bool
    """
    pass

def export_database(filename, row, cur):
    """
    Function to export a single row from csv file as a new record.
    :param filename: Required: str.
    :param row: Required: list.
    :param cur: Required: cursor object.
    :return: Returns a bool.
    """
    pass