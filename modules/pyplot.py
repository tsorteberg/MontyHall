"""
Program: pyplot.py
Author: Tom Sorteberg
Last date modified: 07/28/2020

The purpose of this module is to produce a chart representing data
collected for the Monty Hall Problem.  A str is passed from the calling
method, which is then used to call a csv file of the same name, and
then a bar chart is generated based on that data.
"""
import matplotlib.pyplot as plt
import csv
from constants import constants


def pyplot(filename):
    """
    Function to create to summarize data from csv file and generate bar chart.
    :param filename: Required: str.
    :return: Returns a bool.
    """
    # Define set for input validation.
    character_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ")
    # Input validation.
    if not (character_set.issuperset(filename) and (constants.LOW <= len(filename) <= constants.LENGTH)):
        raise ValueError
    else:
        # Variable declaration and initialization.
        _success = False
        _total_1 = 0
        _total_2 = 0
        _total_3 = 0
        _total_4 = 0
        # Set return variable bool under fail assumption.
        _success = False
        # Attempt to open csv file and sum data.
        try:
            with open(filename + ".csv", 'r') as _csv_file:
                _read_csv = csv.reader(_csv_file, delimiter=',')
                for row in _read_csv:
                    _total_1 += int(row[3])
                    _total_2 += int(row[4])
                    _total_3 += int(row[5])
                    _total_4 += int(row[6])
                _total_win = _total_1 + _total_2
                _total_lose = _total_3 + _total_4
        except FileNotFoundError:
            # Bypass exception to continue program execution.
            pass
        else:
            # Return statement.
            _success = True

        # Generate bar chart.
        if _success:
            # X Axis; dependant variables.
            x = ["Win No Switch", "Win Switch", "Win Total", "Loss No Switch", "Loss Switch", "Loss Total"]
            # Y Axis; independent variables.
            y = [_total_1, _total_2, _total_win, _total_3, _total_4, _total_lose]
            # Plot data.
            plt.bar(x, y, alpha=0.2)
            # Define tick marks.
            plt.yticks(fontsize=8)
            plt.xticks(x, rotation=90, fontsize=8)
            # Adjust windows to display tick marks.
            plt.subplots_adjust(bottom=0.3)
            # Plot text labels.
            for index, value in enumerate(y):
                plt.text(index, value, str(value), ha="center")
            # Define X Axis.
            plt.xlabel('Results', labelpad=10)
            # Define Y Axis.
            plt.ylabel('Number of Trials', labelpad=5)
            # Define Title.
            plt.title('Summary of Trials', fontsize=12)
            # Generate Plot.
            plt.show()

        # Return statement.
        else:
            return _success
