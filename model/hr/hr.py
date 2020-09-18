""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util
import csv

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]
HR_DATABASE = []
ID_INDEX = 0
NAME_INDEX = 1
DOB_INDEX = 2
DEPARTMENT_INDEX = 3
CLEARANCE_INDEX = 4
CURRENT_YEAR = 2020


def read():
    global HR_DATABASE
    HR_DATABASE.clear()
    HR_DATABASE = data_manager.read_table_from_file(DATAFILE, separator=';')           


def write():
    data_manager.write_table_to_file(DATAFILE, HR_DATABASE, separator=';')

    
def get_employees():
    read()
    return HR_DATABASE


def get_employee(employee_id):
    read()
    for employee in HR_DATABASE:
        if employee[ID_INDEX] == employee_id:
            return employee


def add_employee(name, date, department, clearance):
    read()
    new_id = util.generate_id(number_of_small_letters=4, number_of_capital_letters=2, number_of_digits=2, number_of_special_chars=2, allowed_special_chars=r"_+-!")
    HR_DATABASE.append([new_id, name, date, department, clearance])
    write()


def update_employee(employee_id, name, date, department, clearance):
    employee_to_update = get_employee(employee_id)
    employee_to_update[NAME_INDEX] = name
    employee_to_update[DOB_INDEX] = date
    employee_to_update[DEPARTMENT_INDEX] = department
    employee_to_update[CLEARANCE_INDEX] = clearance


def delete_employee(employee_id):
    emp_to_remove = get_employee(employee_id)
    HR_DATABASE.remove(emp_to_remove)


def convert_date(date_as_str):
    y,m,d = date_as_str.split("-")
    return [int(y), int(m), int(d)]
    

def increase_date(any_date):
    current_date = convert_date(any_date)
    num_of_days = 0
    new_date = current_date

    if current_date[1] == 1 or current_date[1] == 3 or current_date[1] == 5 or current_date[1] == 7 or current_date[1] == 8 or current_date[1] == 10 or current_date[1] == 12:
        num_of_days = 31
    elif current_date[1] == 2:
        if current_date[0] % 4 == 0:
            num_of_days = 29
        else:
            num_of_days = 28
    else:
        num_of_days = 30

    if current_date[2] + 14 <= num_of_days:
        new_date[2]= current_date[2] + 14
        return new_date
    else:
        days_till_end_of_month = num_of_days - current_date[2]
        if current_date[1] == 12:
            new_date[0] = current_date[0] + 1
            new_date[1] = 1
            new_date[2] = 14 - days_till_end_of_month
        else:  
            new_date[1] = current_date[1] + 1
            new_date[2] = 14 - days_till_end_of_month

    return new_date





