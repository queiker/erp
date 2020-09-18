from model.crm import crm  # importuje z pliku crm.py
from view import terminal as view

import json
CRM_FILE = 'model/crm/crm.csv'

def list_customers():

    list_of_customers = crm.read()
    view.print_table(list_of_customers, ["id", "name", "email", "subscribed"])
    
def add_customer():
    
    list_of_customers = crm.read()

    #przypisanie do zmiennych danych wprowadzonych przez użytkownika
    id = view.get_input("customer ID")
    name = view.get_input("customer name")
    email = view.get_input("customer email")
    subscribed = view.get_input("customer subscribed [0] or [1]")
    
    
    #dodanie do listy dwówymiarowej listy z danymi wprowadzonymi przez użytkownika
    list_of_customers.append([id, name, email, subscribed])
    
    # #zapisanie listy która zawiera dane z pliku i  wprowadzone od użytkownika
    crm.write(list_of_customers)

def update_customer():
    #poniższy kod otwiera plik z zapisanymi klientami i zapisuje do list_of_customers
    list_of_customers = crm.read()

    #wypisanie na ekranie listy klientów
 
    view.print_table(list_of_customers, ["id", "name", "email", "subscribed"])
    
    #pobranie od użytkownika numeru klienta do zmiany danych
    to_update = view.get_input("number of customer to update : ")
    
    
    #zmiana danych klienta w pętli for
    fields_list = ["id", "name", "email", "subscribed"]
    for c in range(0,4):
        print(list_of_customers[int(to_update)-1][c])
        input_text = f"Put new {fields_list[c]} : "
        nowa_wartosc = view.get_input(input_text)
        if nowa_wartosc != "":
            list_of_customers[int(to_update)-1][c] = nowa_wartosc


    crm.write(list_of_customers)


def delete_customer():
    
    #poniższy kod otwiera plik z zapisanymi klientami i zapisuje do list_of_customers
    list_of_customers = crm.read()

    #wypisanie na ekranie listy klientów
    view.print_table(list_of_customers, ["id", "name", "email", "subscribed"])

    #pobranie od użytkownika numeru klienta do skasowania
    to_pop = view.get_input("number of customer do delete")
    #skasowanie klienta z listy klientów
    list_of_customers.pop(int(to_pop)-1)

    #zapisanie listy z usuniętą pozycją do pliku
    crm.write(list_of_customers)


def get_subscribed_emails():
    list_of_customers = crm.read()

    
    list_of_subscribed = []
    #wypisanie na ekranie listy klientów
    for d in range(0,len(list_of_customers)):
        if list_of_customers[d][3] == "1" :
            list_of_subscribed.append([list_of_customers[d][2]])
            #print(f"({d}) {list_of_customers[d][2]}")

    view.print_table(list_of_subscribed, ["email"])


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
