""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your goes code
    slash = "/"
    backslash = "\\"
    first_line = slash
    end_line = backslash
    dash = "-"
    new_line = "\n"
    DEFAULT_ELEMENT_LENGHT = 8
    i = 0
    j = 0
    list_of_lenghts = []
    separator = "|"
    midlle_of_first_and_last_line = ""
    while i < len(title_list):
        try:
            list_of_lenghts.append(DEFAULT_ELEMENT_LENGHT)
            if list_of_lenghts[i] < len(title_list[i]):
                list_of_lenghts[i] = len(title_list[i])
            
            i += 1
        except IndexError:
            break

    while j < len(table):
        i = 0
        while i < len(table[j]):
            try:
                if len(str(table[j][i])) > list_of_lenghts[i]:
                    list_of_lenghts[i] = len(str(table[j][i]))
                i += 1
            except IndexError:
                break
        j += 1
    i = 0
    while i < len(title_list):
        midlle_of_first_and_last_line += dash * (list_of_lenghts[i] + len(separator))
        i += 1

    except_last_separator_lenght = -1
    midlle_of_first_and_last_line = midlle_of_first_and_last_line[:except_last_separator_lenght]
    first_line += midlle_of_first_and_last_line + backslash
    end_line += midlle_of_first_and_last_line + slash
    header = ""
    newmethod949(title_list, list_of_lenghts, separator)
    header += separator
    body = ""

    j = 0
    while j < len(table):
        i = 0
        k = 0
        line_between = ""
        while k < len(list_of_lenghts):
            line_between += separator + dash * list_of_lenghts[k]
            k += 1
        line_between += separator + new_line
        body += line_between
        while i < len(table[j]):
            try:
                record = str(table[j][i])
                lenght_for_current_record = int(list_of_lenghts[i])
                body += separator + record.center(lenght_for_current_record)
                i += 1
            except IndexError:
                break

        body += separator + new_line
        j += 1
    result = first_line + new_line + header + new_line + body + end_line

    return print(result)

def newmethod293(table, list_of_lenghts, separator, dash, new_line):
    j = 0
    while j < len(table):
        i = 0
        k = 0
        line_between = ""
        while k < len(list_of_lenghts):
            line_between += separator + dash * list_of_lenghts[k]
            k += 1
        line_between += separator + new_line
        body += line_between
        while i < len(table[j]):
            try:
                record = str(table[j][i])
                lenght_for_current_record = int(list_of_lenghts[i])
                body += separator + record.center(lenght_for_current_record)
                i += 1
            except IndexError:
                break

def newmethod949(title_list, list_of_lenghts, separator):
    i = 0
    while i < len(title_list):
        try:
            header_record = title_list[i]
            lenght_for_current_record = int(list_of_lenghts[i])
            header += separator + header_record.center(lenght_for_current_record)
            i += 1
        except IndexError:
            break


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code

    return print(label, result)


def print_boar():
    boar_2 = r'''
                                                                _,-""""-..__
                                                            |`,-'_. `  ` ``  `--'""".
                                                            ;  ,'  | ``  ` `  ` ```  `.
                                                        ,-'   ..-' ` ` `` `  `` `  `  |==.
                                                        ,'    ^    `  `    `` `  ` `.  ;   \
                                                        `}_,-^-   _ .  ` \ `  ` __ `   ;    #
                                                        `"---"' `-`. ` \---""`.`.  `;
                                                                    \\` ;       ; `. `,
                                                                    ||`;      / / | |
                                                                    //_;`    ,_;' ,_;"
      '''
    boar = '''
                888                             
                888                             
                888                             
                88888b.  .d88b.  8888b. 888d888 .d8888b  
                888 "88bd88""88b    "88b888P" 88K 
                888  888888  888.d888888888   "Y8888b.
                888 d88PY88..88P888  888888        X88 
                88888P"  "Y88P" "Y888888888   88888P'
            '''
    print(boar, boar_2)


# print_menu("Customer Menu", options, "Exit to main menu")
def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(f"   {title}:")
    number_of_each_subtitle = 1
    for subtitle in list_options:
        print(f"\t({number_of_each_subtitle}) {subtitle}")
        number_of_each_subtitle += 1
    print(f"\t(0) {exit_message}\n")


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    print(title)
    for each_question in list_labels:
        inputs.append(input(f"{each_question} "))
    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(f"Error: {message}")
