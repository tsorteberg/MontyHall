"""
Program: trial_generator.py
Author: Tom Sorteberg
Last date modified: 07/28/2020

The purpose of this program is to demonstrate the validity of the Monte
Hall Problem.  A GUI will prompt the user to specify the number of trials
to be run and the name of the export file.  After the trials have been run,
the user can view a graph or backup the data to database.
"""
from tkinter import *
from constants import constants
import threading
import subprocess


def validate_trials(trials):
    """
    Function to validate input for trials parameter.
    :param trials: Required: str.
    :return: Returns a bool.
    """
    # Define set for input validation.
    number_set = set("0123456789")
    # Strip input of commas.
    trials = trials.replace(',', '')
    # Input validation.
    if not trials:
        label_status.config(text="ERROR: Number of trials cannot be blank.", fg="red")
        # Return statement.
        return False
    elif not (trials and number_set.issuperset(trials) and isinstance(trials, str) and (
            constants.LOW <= int(trials) <= constants.HIGH)):
        label_status.config(text="ERROR: Number of trials must be between 1-1,000,000.", fg="red")
        # Return statement.
        return False
    else:
        # Return statement.
        return True


def validate_filename(filename):
    """
    Function to validate input for filename parameter.
    :param filename: Required: str.
    :return: Returns a bool.
    """
    # Define set for input validation.
    character_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ")
    # Input validation.
    if not filename:
        label_status.config(text="ERROR: The export file name cannot be blank.", fg="red")
        # Return statement.
        return False
    elif not character_set.issuperset(filename):
        label_status.config(text="ERROR: Export file names must be alpha-numeric.", fg="red")
        # Return statement.
        return False
    elif len(filename) > constants.LENGTH:
        label_status.config(text="ERROR: File length cannot exceed 259 characters.", fg="red")
        # Return statement.
        return False
    else:
        # Return statement.
        return True


def create_objects(trials, filename):
    """
    Driver function to create object of Monty and run specified trials.
    :param trials: Required: str.
    :param filename: Required: str.
    :return: Returns a bool.
    """
    pass

def graph(filename):
    """
    Driver function to create graph.
    :param filename: Required: str.
    :return: No return.
    """
    pass

def create_backup(filename):
    """
    Driver function to backup data from csv file to a database.
    :param filename: Required: str.
    :return: Returns a bool.
    """
    pass

def exit_app():
    pass


# Driver code.
if __name__ == '__main__':
    # GUI object declaration.
    window = Tk()
    window.title("Trial Generator")

    # GUI window configuration.
    window.rowconfigure(0, minsize=15, weight=1)
    window.columnconfigure(1, minsize=15, weight=1)

    # Define and initialize button frame.
    buttons = Frame(window)
    buttons.grid(row=0, column=1, sticky="ns")

    # Define and initialize label and input frame.
    labels = Frame(window)
    labels.grid(row=0, column=0)

    # Define navigation buttons.
    run_button = Button(buttons, text='Run', command=lambda: threading.Thread(target=create_objects, args=(
        input_trials.get(), input_file.get(),)).start(),
                        width=10)
    graph_button = Button(buttons, text='Graph', command=lambda: graph(input_file.get()), width=10)
    backup_button = Button(buttons, text='Backup',
                           command=lambda: threading.Thread(target=create_backup, args=(input_file.get(),)).start(),
                           width=10)
    help_button = Button(buttons, text='Help', command=lambda: subprocess.Popen(["help.pdf"], shell=True), width=10)
    exit_button = Button(buttons, text='Exit', command=lambda: exit_app(), width=10)

    # Initialize navigation buttons.
    run_button.grid(row=0, column=1, sticky="nw", padx=10, pady=5)
    graph_button.grid(row=1, column=1, sticky="nw", padx=10, pady=5)
    backup_button.grid(row=2, column=1, sticky="nw", padx=10, pady=5)
    help_button.grid(row=3, column=1, sticky="nw", padx=10, pady=5)
    exit_button.grid(row=4, column=1, sticky="nw", padx=10, pady=5)

    # Define labels.
    label_prompt = Label(labels, text="Status:", anchor="w", width=10)
    label_status = Label(labels, text="Enter number of trials (1-1,000,000).", anchor="w", width=45)

    # Initialize labels.
    label_prompt.grid(row=0, column=0, padx=10, pady=5, sticky="nw")
    label_status.grid(row=1, column=0, padx=10, pady=5, sticky="nw")

    # Define input boxes.
    label_trials = Label(labels, text="Number of trials:")
    input_trials = Entry(labels, width=10)
    label_file = Label(labels, text="Export csv filename:")
    input_file = Entry(labels, width=50)

    # Initialize input boxes.
    label_trials.grid(row=2, column=0, padx=10, sticky="nw")
    input_trials.grid(row=3, column=0, padx=10, sticky="nw")
    label_file.grid(row=4, column=0, padx=10, sticky="nw")
    input_file.grid(row=5, column=0, padx=10, sticky="nw")

    window.protocol("WM_DELETE_WINDOW", exit_app)

    # Loop for GUI input.
    window.mainloop()
