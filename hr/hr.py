""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
import time


HR_FILE = "hr/persons.csv"


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    while True:
        handle_menu_account()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(HR_FILE)
    elif option == "2":
        add(HR_FILE)
    elif option == "3":
        inputs_id = ui.get_inputs(["ID"], "Input ID to remove: ")
        remove(HR_FILE, inputs_id[0])
    elif option == "4":
        inputs_id = ui.get_inputs(["ID"], "Input ID to remove: ")
        update(HR_FILE, inputs_id[0])
    elif option == "0":
        common.returning_to_main_menu()
    else:
        raise KeyError("There is no such option.")


def handle_menu_account():
    options = ["Show Table",
               "Add something into table",
               "Remove something from table",
               "Update table"]
    ui.print_menu("Human resources", options, "Exit to main menu")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    titles = ["ID", "Name", "Birth year"]
    hr_table = data_manager.get_table_from_file(table)
    return ui.print_table(hr_table, titles)


def checking_M_D_Y(list_to_check, question_number, date_since, date_to, which_question):
    if not list_to_check[question_number].isdigit() or not date_since < int(list_to_check[question_number]) < date_to:
        ui.print_error_message(f"Please write correct answer for question {which_question}. It must be an integer")
        
        return "ERROR"


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    ID = common.generate_random(table)
    elements_to_add = ["Name", "Birth year"]
    inputs = ui.get_inputs(elements_to_add, "Please answer: ")
    
    list_of_checks = [checking_M_D_Y(inputs, 1, 0, 2020, "Birth year")]
    time.sleep(1)
    if "ERROR" in list_of_checks:
        return table
    
    our_file_to_edit = open(f"{table}", "a")
    inputs.insert(0, f"{ID}")
    our_file_to_edit.write(";".join(inputs) + "\n")
    our_file_to_edit.close()
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    readed_file = data_manager.get_table_from_file(table)
    POSITION_OF_ID = 0
    i = 0

    while i < len(readed_file):
        if id_ == readed_file[i][POSITION_OF_ID]:
            readed_file.remove(readed_file[i])
        i += 1
    data_manager.write_table_to_file(table, readed_file)

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    readed_file = data_manager.get_table_from_file(table)
    POSITION_OF_ID = 0
    i = 0

    while i < len(readed_file):
        if id_ == readed_file[i][POSITION_OF_ID]:
            elements_to_update = ["Name", "Birth year"]
            inputs = ui.get_inputs(elements_to_update, "Please answer: ")
            list_of_checks = [checking_M_D_Y(inputs, 1, 0, 2020, "Birth year")]
            if "ERROR" in list_of_checks:
                return table
            inputs.insert(0, id_)
            readed_file.remove(readed_file[i])
            readed_file.insert(i, inputs)
        i += 1
    data_manager.write_table_to_file(table, readed_file)

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
