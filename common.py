""" Common module
implement commonly used functions here
"""

import random
import string
import main


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """
    # vH34Ju#&
    FIRST_ELEMENT = 0
    SECOND_ELEMENT = 1
    id_uniqueness = 0
    POSITION_OF_ID_IN_TABLE = 0
    TWO_RANDOM_CHARACTERS = 2
    list_of_all_ids = []
    i = 0
    while i < len(table):
        list_of_all_ids.append(table[i][POSITION_OF_ID_IN_TABLE])
        i += 1

    while not id_uniqueness:
        random_lowercase_list = [char for char in random.choices(string.ascii_lowercase, k=TWO_RANDOM_CHARACTERS)]
        random_uppercase_list = [char for char in random.choices(string.ascii_uppercase, k=TWO_RANDOM_CHARACTERS)]
        random_digit_list = [char for char in random.choices(string.digits, k=TWO_RANDOM_CHARACTERS)]
        list_of_characters = list(string.punctuation)
        list_of_characters.remove(";")
        random_char = [char for char in random.choices(list_of_characters, k=TWO_RANDOM_CHARACTERS)]

        generated = random_lowercase_list[FIRST_ELEMENT] + random_uppercase_list[FIRST_ELEMENT]\
            + random_digit_list[FIRST_ELEMENT] + random_digit_list[SECOND_ELEMENT]\
            + random_uppercase_list[SECOND_ELEMENT] + random_lowercase_list[SECOND_ELEMENT]\
            + random_char[FIRST_ELEMENT] + random_char[SECOND_ELEMENT]
        if generated in list_of_all_ids:
            continue
        else:
            id_uniqueness = 1
    return generated


def returning_to_main_menu():
    return main.main()
