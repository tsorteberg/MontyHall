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
from definitions import monty
from modules import pyplot, database
import threading
import subprocess
import csv
import sqlite3


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
        label_status.config(text="ERROR: Number of trials cannot be blank.",
                            fg="red")
        # Return statement.
        return False
    elif not (trials and number_set.issuperset(trials)
              and isinstance(trials, str)
              and (constants.LOW <= int(trials) <= constants.HIGH)):
        label_status.config(text="ERROR: Number of trials must be between 1-1,000,000.",
                            fg="red")
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
    character_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01"
                        "23456789 ")
    # Input validation.
    if not filename:
        label_status.config(text="ERROR: The export file name cannot be blank.",
                            fg="red")
        # Return statement.
        return False
    elif not character_set.issuperset(filename):
        label_status.config(text="ERROR: Export file names must be alpha-numeric.",
                            fg="red")
        # Return statement.
        return False
    elif len(filename) > constants.LENGTH:
        label_status.config(text="ERROR: File length cannot exceed 259 characters.",
                            fg="red")
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
    trials = trials.replace(',', '')
    # Input Validation for trials parameter.
    if validate_trials(trials) and validate_filename(filename):

        # Cast str trials parameter to int.
        _trial_int = int(trials)
        # Instantiate Monty object.
        _trials = monty.Monty(_trial_int)
        # Function call to create csv file.
        _message = _trials.create_csv(filename)
        # Set return variable bool under fail assumption.
        _success = False
        # Execute trials and export to csv.
        if _message:

            # Disable buttons until complete.
            run_button.config(state="disabled")
            graph_button.config(state="disabled")
            backup_button.config(state="disabled")
            help_button.config(state="disabled")
            exit_button.config(state="disabled")
            input_trials.config(state="disabled")
            input_file.config(state="disabled")

            # Function call for run_trials.
            # Set index to zero.
            _index = 0
            # For loop to execute trials.
            for x in range(_trial_int):
                # Set unique identifier.
                _index += 1
                # Temp variable used to export to csv.
                _temp = _trials.run_trial(_index)
                # Export to csv.
                _trials.export_csv(_temp, filename)
                # Calculate progress.
                _progress = (_index / _trial_int) * 100
                # Update label displaying progress.
                label_status.config(text="Processing trials: "
                                         + '{0:.2f}'.format(_progress)
                                         + " %", fg="black")
            # Update label upon completion.
            label_status.config(text=str("{:,}".format(_trial_int))
                                + " trials processed successfully.")
            # If successful, return True.
            _success = True

            # Enable buttons after completion.
            run_button.config(state="active")
            graph_button.config(state="active")
            backup_button.config(state="active")
            help_button.config(state="active")
            exit_button.config(state="active")
            input_trials.config(state="normal")
            input_file.config(state="normal")

        else:
            # If file exists, update status label.
            label_status.config(text="ERROR: The file already exists.",
                                fg="red")

        # Return statement.
        return _success


def graph(filename):
    """
    Driver function to create graph.
    :param filename: Required: str.
    :return: No return.
    """
    # Input validation.
    if validate_filename(filename):
        # Function call to generate plot.
        test = pyplot.pyplot(filename)
        if test:
            # Bypass exception to continue program execution.
            pass
        else:
            # If fail, update statud label.
            label_status.config(text="ERROR: The file does not exist.",
                                fg="red")


def create_backup(filename):
    """
    Driver function to backup data from csv file to a database.
    :param filename: Required: str.
    :return: Returns a bool.
    """
    # Input Validation.
    if not validate_filename(filename):
        pass
    elif not database.check_csv(filename):
        label_status.config(text="The import csv file '" + filename + "' cannot be found", fg="red")
    elif not database.connect_database():
        label_status.config(text="ERROR: Unable to connect to database.", fg="red")
    elif not database.create_tables(filename):
        label_status.config(text="Unable to create table.", fg="red")
    else:

        # Disable buttons until complete.
        run_button.config(state="disabled")
        graph_button.config(state="disabled")
        backup_button.config(state="disabled")
        help_button.config(state="disabled")
        exit_button.config(state="disabled")
        input_trials.config(state="disabled")
        input_file.config(state="disabled")

        # Count rows in csv file.
        with open(filename + ".csv", 'r') as file:
            reader = csv.reader(file)
            lines = len(list(reader))

        # Import csv file to database.
        with open(filename + '.csv', 'r') as read_obj:
            # Open csv file for import.
            csv_reader = csv.reader(read_obj)
            # Open database connection.
            conn = sqlite3.connect("backup.db")
            # Define cursor.
            cur = conn.cursor()
            try:
                # Set return variable bool under fail assumption.
                _success = False
                # Define index.
                _index = 0
                # For loop for database backup.
                for row in csv_reader:
                    # Increment index.
                    _index += 1
                    # Method call to insert record into database.
                    database.export_database(filename, row, cur)
                    # Calculate progress.
                    _progress = (_index / lines) * 100
                    # Update label displaying progress.
                    label_status.config(text="Processing Backup: " + '{0:.2f}'.format(_progress) + " %",
                                        fg="black")
            except sqlite3.IntegrityError:
                # Bypass exception to continue program execution.
                pass
            else:
                # If backup is successful, return True.
                _success = True

        if _success:
            # Update status label.
            label_status.config(text="Data backup successful.")
        else:
            # Update status label.
            label_status.config(text="ERROR: Duplicate data found; backup aborted.", fg="red")

    # Enable buttons after completion.
    run_button.config(state="active")
    graph_button.config(state="active")
    backup_button.config(state="active")
    help_button.config(state="active")
    exit_button.config(state="active")
    input_trials.config(state="normal")
    input_file.config(state="normal")

    # Commit changes to database.
    conn.commit()
    # Close database connection.
    conn.close()

    # Return statement.
    return _success


def exit_app():
    """
    Function for application exit.
    :return: Return not possible.
    """
    # Destroy Window.
    window.destroy()
    # Force termination of application.
    sys.exit()


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

#                      Test Case Coverage: Unit Test                          #
#          Input             Expected Output            Actual Output         #
#       Run:10000,"test"         Success                    Success           #
#     Graph:10000,"test"         Success                    Success           #
#    Backup:10000,"test"         Success                    Success           #
