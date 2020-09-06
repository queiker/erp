from model.crm import crm  # importuje z pliku crm.py
from view import terminal as view

import json
CRM_FILE = 'model/crm/database.txt'

def list_customers():
    list_of_customers = crm.open_file(CRM_FILE)
    #wypisanie na ekranie 
    for i in range(0,len(list_of_customers)):
        #print(list_of_customers[i]) stary kod
        view.print_message(f"({i}) {list_of_customers[i]}")


def add_customer():
    
    list_of_customers = crm.open_file(CRM_FILE)

    #przypisanie do zmiennych danych wprowadzonych przez użytkownika
    name = view.get_input("Put customer name : ")
    second_name = view.get_input("Put customer second name : ")
    adress = view.get_input("Put customer adress : ")
    post_code = view.get_input("Put customer post code : ")
    city = view.get_input("Put customer city : ")
    email_adress = view.get_input("Put customer email adress : ")
    email_subscription = view.get_input("Put customer email subscription [yes] or [no] : ")
    nationality = view.get_input("Put customer nationality : ")
    
    #dodanie do listy dwówymiarowej listy z danymi wprowadzonymi przez użytkownika
    list_of_customers.append(['000',name,second_name,adress,post_code,city,email_adress,email_subscription,nationality])
    
    #zapisanie listy która zawiera dane z pliku i  wprowadzone od użytkownika
    crm.save_file(CRM_FILE, list_of_customers)

def update_customer():
    #poniższy kod otwiera plik z zapisanymi klientami i zapisuje do list_of_customers
    list_of_customers = crm.open_file(CRM_FILE)

    #wypisanie na ekranie listy klientów
    for d in range(0,len(list_of_customers)):
        view.print_message(f"({d}) {list_of_customers[d]}")
    #pobranie od użytkownika numeru klienta do zmiany danych
    to_update = input("Put number of customer to update : ")
    
    
    #zmiana danych klienta w pętli for
    fields_list = ["ID","NAME","SECOND NAME","ADRES","POST CODE","CITY","EMAIL ADRESS","EMAIL SUBSCRIPTION","NATIONALITY"]
    for c in range(1,9):
        print(list_of_customers[int(to_update)][c])
        input_text = f"Put new {fields_list[c]} : "
        nowa_wartosc = input(input_text)
        if nowa_wartosc != "":
            list_of_customers[int(to_update)][c] = nowa_wartosc

    # print(list_of_customers[int(to_update)][2])
    # nowa_wartosc = input("Put new second name : ")
    # if nowa_wartosc != "":
    #     list_of_customers[int(to_update)][2] = nowa_wartosc

    # print(list_of_customers[int(to_update)][3])
    # nowa_wartosc = input("Put new adress : ")
    # if nowa_wartosc != "":
    #     list_of_customers[int(to_update)][3] = nowa_wartosc

    # print(list_of_customers[int(to_update)][4])
    # nowa_wartosc = input("Put new post code : ")
    # if nowa_wartosc != "":
    #     list_of_customers[int(to_update)][4] = nowa_wartosc

    # print(list_of_customers[int(to_update)][5])
    # nowa_wartosc = input("Put new city : ")
    # if nowa_wartosc != "":
    #     list_of_customers[int(to_update)][5] = nowa_wartosc

    # print(list_of_customers[int(to_update)][6])
    # nowa_wartosc = input("Put new email : ")
    # if nowa_wartosc != "":
    #     list_of_customers[int(to_update)][6] = nowa_wartosc

    # print(list_of_customers[int(to_update)][7])
    # nowa_wartosc = input("Subscription [yes] or [no] : ")
    # if nowa_wartosc != "":
    #     list_of_customers[int(to_update)][7] = nowa_wartosc

    # print(list_of_customers[int(to_update)][8])
    # nowa_wartosc = input("Put new nationality [Polish] : ")
    # if nowa_wartosc != "":
    #     list_of_customers[int(to_update)][8] = nowa_wartosc



    crm.save_file(CRM_FILE, list_of_customers)

    # #zapisanie listy z usuniętą pozycją do pliku
    # data = {}
    # data['customers_list'] = []
    # for d in range(0, len(list_of_customers) ):
    #     data['customers_list'].append({
    #         'ID': list_of_customers[d][0],
    #         'name': list_of_customers[d][1],
    #         'second_name': list_of_customers[d][2],
    #         'adress': list_of_customers[d][3],
    #         'post_code': list_of_customers[d][4],
    #         'city': list_of_customers[d][5],
    #         'email_adress': list_of_customers[d][6],
    #         'email_subscription': list_of_customers[d][7],
    #         'nationality': list_of_customers[d][8]
    #     })
    # with open(CRM_FILE, 'w') as outfile:
    #     json.dump(data, outfile)



def delete_customer():
    #view.print_error_message("Not implemented yet.")
    
    #poniższy kod otwiera plik z zapisanymi klientami i zapisuje do list_of_customers
    customer_counter = 0
    with open(CRM_FILE) as json_file: #TODO:Trzeba zmienić nazwę pliku na CRM
        data = json.load(json_file)
        list_of_customers = []
        #poniżej zapisanie danych z pliku do list_of_customers
        for p in data['customers_list']:
            list_of_customers.append([p['ID'],p['name'],p['second_name'],p['adress'],p['post_code'],p['city'],p['email_adress'],p['email_subscription'],p['nationality'] ])
            customer_counter += 1

    #wypisanie na ekranie listy klientów
    for d in range(0,len(list_of_customers)):
        print(f"({d}) {list_of_customers[d]}")
    #pobranie od użytkownika numeru klienta do skasowania
    to_pop = input("Put number of customer do delete : ")
    #skasowanie klienta z listy klientów
    list_of_customers.pop(int(to_pop))

    #zapisanie listy z usuniętą pozycją do pliku
    data = {}
    data['customers_list'] = []
    for d in range(0, len(list_of_customers) ):
        data['customers_list'].append({
            'ID': list_of_customers[d][0],
            'name': list_of_customers[d][1],
            'second_name': list_of_customers[d][2],
            'adress': list_of_customers[d][3],
            'post_code': list_of_customers[d][4],
            'city': list_of_customers[d][5],
            'email_adress': list_of_customers[d][6],
            'email_subscription': list_of_customers[d][7],
            'nationality': list_of_customers[d][8]
        })
    with open(CRM_FILE, 'w') as outfile:
        json.dump(data, outfile)





def get_subscribed_emails():
    #poniższy kod otwiera plik z zapisanymi klientami i zapisuje do list_of_customers
    customer_counter = 0
    with open(CRM_FILE) as json_file: #TODO:Trzeba zmienić nazwę pliku na CRM
        data = json.load(json_file)
        list_of_customers = []
        #poniżej zapisanie danych z pliku do list_of_customers
        for p in data['customers_list']:
            list_of_customers.append([p['ID'],p['name'],p['second_name'],p['adress'],p['post_code'],p['city'],p['email_adress'],p['email_subscription'],p['nationality'] ])
            customer_counter += 1

    #wypisanie na ekranie listy klientów
    for d in range(0,len(list_of_customers)):
        if list_of_customers[d][7] == "yes" :
            print(f"({d}) {list_of_customers[d][6]}")


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
