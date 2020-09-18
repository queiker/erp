""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager

DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]

def read():
    CRM_DATABASE = []
    CRM_DATABASE.clear()
    CRM_DATABASE = data_manager.read_table_from_file(DATAFILE, separator=';') 
    return CRM_DATABASE          

def write(CRM_DATABASE):
    data_manager.write_table_to_file(DATAFILE, CRM_DATABASE, separator=';')
