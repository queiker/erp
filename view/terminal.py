def print_menu(title, list_options):
    
    print(f"{title}\n")
    for i in range(1, len(list_options)):
        print(f"({i}) {list_options[i]}")
    print(f"(0) {list_options[0]}")
       
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    pass


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)
    


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    print()
    if type(result) == float:        
        formatted_float = "{:.2f}".format(result)
        print(f'{label}: {formatted_float}')        
    elif type(result) == int:
        print(f'{label}: {result}')        
    elif type(result) == list or type(result) == tuple:
        print(f'{label}:')
        k = 1
        for i in result:
            print(f'{i}',end="" )
            if k != len(result):
                print(f'; ',end="")
                k+=1
        print()        
    elif type(result) == dict:
        print(label)
        k=1
        for elem in result:
            print(f'{elem}: {result[elem]}', end="") 
            if k != len(result):
                print(f'; ',end="")
                k+=1
        print()        
    print()
    

# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
              
def print_table(table, headers):
    lista = []
    lista.append(headers)
    max_len_elm = 0

    for i in table:
        lista.append(i)
    for elem in headers:
        if len(elem) > max_len_elm:
            max_len_elm = len(elem)
    for items in table:
        for _ in items:
            if len(_) > max_len_elm:
                max_len_elm = len(_)

    for index, row in enumerate(lista, 0):
        if index == 0:
            n = 0
            print(f"/---", end="")
            for column in row:
                n += max_len_elm+2
            n -= 1
            print("-" * n + "\ ")
        else:
            print(f'|--|', end="")
            for column in row:
                print("-" * (max_len_elm+1) + '|', end="")
            print()
        if index == 0:
            print(f'|  |', end="")
        else:
            print(f'|{index:2}|', end="")
        for column in row:
            print(f'{column:{max_len_elm +1}}|', end="")
        print()

        if index == len(lista)-1:
            n = 0
            print(f"\---", end="")
            for column in row:
                n += max_len_elm+2
            n -= 1
            print("-"*n + "/ ") 

    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """



def get_input(label):
    
    result = input(f'Please enter {label}: ')
    
    return result


def get_inputs(labels):
    result = []
    for i in labels:
        inp = input(f'Please enter {i}')
        result.append(inp)
    return result
 
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    
def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(message)

