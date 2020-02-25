""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

SALES_FILE = "sales/sales.csv"


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
        show_table(SALES_FILE)
    elif option == "2":
        add(SALES_FILE)
    elif option == "3":
        inputs_id = ui.get_inputs(["ID"], "Input ID to remove: ")
        remove(SALES_FILE, inputs_id[0])
    elif option == "4":
        inputs_id = ui.get_inputs(["ID"], "Input ID to remove: ")
        update(SALES_FILE, inputs_id[0])
    elif option == "0":
        common.returning_to_main_menu()
    else:
        raise KeyError("There is no such option.")


def handle_menu_account():
    options = ["Show Table",
               "Add something into table",
               "Remove something from table",
               "Update table"]
    ui.print_menu("Sales menu", options, "Exit to main menu")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    titles = ["ID", "Title", "Price", "Month", "Day", "Year"]
    sales_table = data_manager.get_table_from_file(table)
    return ui.print_table(sales_table, titles)


def checking_M_D_Y(list_to_check, question_number, date_since, date_to, which_question):
    if not list_to_check[question_number].isdigit() or not date_since < int(list_to_check[question_number]) < date_to:
        ui.print_error_message(f"Please write correct answer for question {which_question}")
        return "ERROR"


def checking_price(list_to_check, which_question):
    if not list_to_check[1].isdigit():
        ui.print_error_message(f"Please write correct answer for question {which_question}")
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
    elements_to_add = ["Title", "Price", "Month", "Day", "Year"]
    inputs = ui.get_inputs(elements_to_add, "Please answer: ")

    list_of_checks = [checking_M_D_Y(inputs, 2, 0, 13, "Month"),
                      checking_M_D_Y(inputs, 3, 0, 32, "Day"),
                      checking_M_D_Y(inputs, 4, 0, 2020, "Year"),
                      checking_price(inputs, "Price")]

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
            elements_to_update = ["Title", "Price", "Month", "Day", "Year"]
            inputs = ui.get_inputs(elements_to_update, "Please answer: ")
            list_of_checks = [checking_M_D_Y(inputs, 2, 0, 13, "Month"),
                              checking_M_D_Y(inputs, 3, 0, 32, "Day"),
                              checking_M_D_Y(inputs, 4, 0, 2020, "Year"),
                              checking_price(inputs, "Price")]
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

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
