""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
import time

STORE_FILE = "store/games.csv"


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
        show_table(STORE_FILE)
    elif option == "2":
        add(STORE_FILE)
    elif option == "3":
        inputs_id = ui.get_inputs(["ID"], "Input ID to remove: ")
        remove(STORE_FILE, inputs_id[0])
    elif option == "4":
        inputs_id = ui.get_inputs(["ID"], "Input ID to remove: ")
        update(STORE_FILE, inputs_id[0])
    elif option == "5":
        get_counts_by_manufacturers(STORE_FILE)
    elif option == "6":
        inputs_manu = ui.get_inputs(["Manufacturer"], "Input name of manufacturer: ")
        get_average_by_manufacturer(STORE_FILE, inputs_manu[0])
    elif option == "0":
        common.returning_to_main_menu()
    else:
        raise KeyError("There is no such option.")


def handle_menu_account():
    options = ["Show Table",
               "Add something into table",
               "Remove something from table",
               "Update table",
               'How many different kinds of game are available of each manufacturer',
               'What is the average amount of games in stock of a given manufacturer?']
    ui.print_menu("Store menu", options, "Exit to main menu")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    titles = ["ID", "Title", "Manufacturer", "Price", "In stock"]
    store_table = data_manager.get_table_from_file(table)
    return ui.print_table(store_table, titles)


def checking_in_stock(list_to_check, which_question):
    if not list_to_check[3].isdigit():
        ui.print_error_message(f"Please write correct answer for question {which_question}")
        return "ERROR"


def checking_price(list_to_check, which_question):
    if not list_to_check[2].isdigit():
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
    elements_to_add = ["Title", "Manufacturer", "Price", "In stock"]
    inputs = ui.get_inputs(elements_to_add, "Please answer: ")

    list_of_checks = [checking_in_stock(inputs, "In stock"),
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
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    readed_file = data_manager.get_table_from_file(table)
    POSITION_OF_ID = 0
    i = 0

    while i < len(readed_file):
        if id_ == readed_file[i][POSITION_OF_ID]:
            elements_to_update = ["Title", "Manufacturer", "Price", "In stock"]
            inputs = ui.get_inputs(elements_to_update, "Please answer: ")
            list_of_checks = [checking_in_stock(inputs, "In stock"),
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

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    readed_file = data_manager.get_table_from_file(table)
    POSITION_OF_MANUFACTURER = 2
    i = 0
    manufacturer_dict = {}
    starting_game_number = 1
    while i < len(readed_file):
        manufacturer_name = readed_file[i][POSITION_OF_MANUFACTURER]
        if manufacturer_name in manufacturer_dict.keys():
            manufacturer_dict[manufacturer_name] += 1
        else:
            manufacturer_dict[manufacturer_name] = starting_game_number
        i += 1
    for k, v in manufacturer_dict.items():
        ui.print_result(f'{v} diffrent games', f"{k} has ")
    time.sleep(2)
    return table


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    readed_file = data_manager.get_table_from_file(table)
    POSITION_OF_MANUFACTURER = 2
    POSITION_OF_STOCK = 4
    i = 0
    number_of_games = []
    sum_of_games = 0
    lenght_of_number_of_games_list = 0
    while i < len(readed_file):
        manufacturer_name = readed_file[i][POSITION_OF_MANUFACTURER]
        amount_of_game = readed_file[i][POSITION_OF_STOCK]
        if manufacturer == manufacturer_name:
            number_of_games.append(amount_of_game)
        i += 1
    lenght_of_number_of_games_list = len(number_of_games)
    if lenght_of_number_of_games_list == 0:
        ui.print_result("Sorry, manufacturer not found", "")
    else:
        for num in number_of_games:
            sum_of_games += int(num)
        result = sum_of_games / lenght_of_number_of_games_list
        ui.print_result(f'is {result}', f"Average number of games for {manufacturer}")
    time.sleep(2)
    return table
