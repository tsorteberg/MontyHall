"""
Program: monty.py
Author: Tom Sorteberg
Last date modified: 07/28/2020

The purpose of this class file is to define an object type of Monty,
which will have a int member called trial, and several methods used
to solve the Monty Hall Problem.  The input is provided via a parameter
passed from the calling function; returns a str, int, or bool.
"""

"""Class Monty"""


class Monty:

    def __init__(self, trials):
        """
        Default constructor.
        :param trials: Required: int
        """
        pass

    def set_trials(self, trials):
        """
        Set function for trials member.
        :param trials: Required: Set as private int.
        :return: No return for set function.
        """
        pass

    def get_trials(self):
        """
        Get function for trials member.
        :return: Returns an int.
        """
        pass

    def run_trial(self, index):
        """
        Function to perform single trial.
        :param index: Required: int.
        :return: Returns a tuple.
        """
        pass

    def create_csv(self, filename):
        """
        Function to create csv file for export.
        :param filename: Required: str.
        :return: Returns a bool.
        """
        pass

    def export_csv(self, product, filename):
        """
        Function to perform export to csv for single trial.
        :param product: Required: tuple.
        :param filename: Required: str.
        :return: Returns a bool.
        """
        pass

    def __str__(self):
        """
        Default return to string.
        :return: Returns a str.
        """
        pass

    def __repr__(self):
        """
        Default return to string for debugging purposes.
        :return: Returns a str.
        """
        pass
