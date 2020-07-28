"""
Program: monty.py
Author: Tom Sorteberg
Last date modified: 07/28/2020

The purpose of this class file is to define an object type of Monty,
which will have a int member called trial, and several methods used
to solve the Monty Hall Problem.  The input is provided via a parameter
passed from the calling function; returns a str, int, or bool.
"""
from constants import constants
"""Class Monty"""


class Monty:

    def __init__(self, trials):
        """
        Default constructor.
        :param trials: Required: int
        """
        # Input Validation.
        if not isinstance(trials, int):
            raise Exception
        elif not constants.LOW <= trials <= constants.HIGH:
            raise Exception
        else:
            # Set trials member.
            self._trials = trials

    def set_trials(self, trials):
        """
        Set function for trials member.
        :param trials: Required: Set as private int.
        :return: No return for set function.
        """
        # Strip input of commas.
        trials = trials.replace(',', '')
        # Input Validation.
        if not isinstance(trials, int):
            raise Exception
        elif not constants.LOW <= trials <= constants.HIGH:
            raise Exception
        else:
            self._trials = trials

        # Return Statement.
        return None

    def create_csv(self, filename):
        """
        Function to create csv file for export.
        :param filename: Required: str.
        :return: Returns a bool.
        """
        # Define set for input validation.
        character_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ")
        # Input Validation.
        if not (character_set.issuperset(filename) and (constants.LOW <= len(filename) <= constants.LENGTH)):
            # Raises ValueError.
            raise ValueError
        else:
            # Set return variable bool under fail assumption.
            _success = False
            # Attempt to create csv file.
            try:
                _create_file = open(filename + ".csv", 'x')
            except FileExistsError:
                # Bypass exception to continue program execution.
                pass
            else:
                # If file creation is successful, return true.
                _success = True

            # Return Statement.
            # If file create fails, return default value.
            return _success

    def get_trials(self):
        """
        Get function for trials member.
        :return: Returns an int.
        """

        # Return Statement.
        return self._trials

    def run_trial(self, index):
        """
        Function to perform single trial.
        :param index: Required: int.
        :return: Returns a tuple.
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
