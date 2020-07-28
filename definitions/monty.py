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
import random
from datetime import datetime
import csv
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
        character_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy"
                            "z0123456789 ")
        # Input Validation.
        if not (character_set.issuperset(filename)
                and (constants.LOW <= len(filename) <= constants.LENGTH)):
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
        # Input Validation.
        if not (isinstance(index, int)
                and (constants.LOW <= int(index) <= constants.HIGH)):
            raise ValueError
        else:
            # Declare and initialize variables.
            _choices = [1, 2, 3]
            _switch_choice = [1, 2, 3]
            _correct = random.randint(constants.CHOICE_LOW,
                                      constants.CHOICE_HIGH)
            _choice = random.randint(constants.CHOICE_LOW,
                                     constants.CHOICE_HIGH)
            # Selection logic for random trial generation.
            for num in _choices:
                if _correct == num:
                    _choices.remove(num)
            for num in _choices:
                if _choice == num:
                    _choices.remove(num)
            if len(_choices) == constants.CHOICE_LOW:
                _reveal = int(_choices[0])
            else:
                _reveal = random.choice([_choices[0], _choices[1]])
            for num in _switch_choice:
                if _reveal == num:
                    _switch_choice.remove(num)
            _switch = random.choice([_switch_choice[0], _switch_choice[1]])
            # Selection logic to define case outcome.
            if _switch == _correct:
                if _switch == _choice:
                    _option = 1
                else:
                    _option = 2
            else:
                if _switch == _choice:
                    _option = 3
                else:
                    _option = 4

            # Define internal function.
            def switch(_option):
                """
                Internal switch case function providing case matching to pass
                to csv file.
                :param _option: Required: int.
                :return: Returns a list of int.
                """
                # Variable cases declaration.
                cases = {
                    1: [1, 0, 0, 0],
                    2: [0, 1, 0, 0],
                    3: [0, 0, 1, 0],
                    4: [0, 0, 0, 1]
                }

                # Return Statement
                return cases.get(_option)
            # Variable declaration and initialization for product output.
            _date = datetime.now()
            _results = {"Correct": _correct, "Choice": _choice,
                        "Reveal": _reveal, "Switch": _switch}
            _case = switch(_option)

            # Variable declaration and initialization of product output.
            _product = (index, _date, _results, _case)
            # Return statement.
            return _product

    def export_csv(self, product, filename):
        """
        Function to perform export to csv for single trial.
        :param product: Required: tuple.
        :param filename: Required: str.
        :return: Returns a bool.
        """
        # Define set for input validation.
        character_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ")
        # Input validation.
        if not (character_set.issuperset(filename) and (constants.LOW <= len(filename) <= constants.LENGTH)) or isinstance(product, list):
            raise ValueError
        else:
            # Set return variable bool under fail assumption.
            _success = False
        # Attempt to write trial list to file.
        try:
            with open(filename + ".csv", 'a', newline="") as _csv_file:
                _file_writer = csv.writer(_csv_file, delimiter=',')
                _file_writer.writerow([product[0], product[1], product[2], product[3][0], product[3][1], product[3][2], product[3][3]])
        except FileExistsError:
            # Bypass exception to continue program execution.
            pass
        else:
            # If import is successful, return true.
            _success = True

        # Return Statement.
        # If file create fails, return default value.
        return _success

    def __str__(self):
        """
        Default return to string.
        :return: Returns a str.
        """

        # Return Statement.
        return "Trials: " + str(self._trials)

    def __repr__(self):
        """
        Default return to string for debugging purposes.
        :return: Returns a str.
        """

        # Return Statement
        return "Monty(" + str(self._trials) + ")"
