""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""
import json
from model import data_manager, util


# DATAFILE = "model/crm/crm.csv"
# HEADERS = ["id", "name", "email", "subscribed"]


def open_file(DATAFILE):

    #poniższy kod otwiera plik z zapisanymi klientami i zapisuje do list_of_customers
    customer_counter = 0
    with open(DATAFILE) as json_file: #TODO:Trzeba zmienić nazwę pliku na CRM
        data = json.load(json_file)
        list_of_customers = []
        #poniżej zapisanie danych z pliku do list_of_customers
        for p in data['customers_list']:
            list_of_customers.append([p['ID'],p['name'],p['second_name'],p['adress'],p['post_code'],p['city'],p['email_adress'],p['email_subscription'],p['nationality'] ])
            customer_counter += 1
    return list_of_customers

def save_file(DATAFILE, list):
    #zapisanie listy która zawiera dane z pliku i  wprowadzone od użytkownika
    data = {}
    data['customers_list'] = []
    for d in range(0, len(list) ):
        data['customers_list'].append({
            'ID': list[d][0],
            'name': list[d][1],
            'second_name': list[d][2],
            'adress': list[d][3],
            'post_code': list[d][4],
            'city': list[d][5],
            'email_adress': list[d][6],
            'email_subscription': list[d][7],
            'nationality': list[d][8]
        })
    with open(DATAFILE, 'w') as outfile:
        json.dump(data, outfile)

