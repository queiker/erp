from model.hr import hr
from view import terminal as view


def list_employees():
    hr.read()
    view.print_table(hr.HR_DATABASE, hr.HEADERS)

def add_employee():
    responses = view.get_inputs(["Put employee name: ", "Put employee date of birth in format YYYY-MM-DD: ",
                                 "Put employee department: ",  "Put Clearance: "])
    hr.add_employee(responses[0], responses[1], responses[2], responses[3])
    


def update_employee():
    list_employees()
    number = int(view.get_input("Choose employee to update(e.g. 1): "))
    employee = hr.get_employees()[number-1]
    employee_id = hr.get_employees()[number-1][0]
    responses = view.get_inputs(["Update name(leave empty if there are no changes): ", "Update date of birth in format YYYY-MM-DD(leave empty if there are no changes): ",
                                 "Update department(leave empty if there are no changes): ",  "Update Clearance(leave empty if there are no changes): "])

    for i in range(len(responses)):
        if responses[i] == "":
            responses[i]= employee[i+1]
    
    hr.update_employee(employee_id, responses[0], responses[1], responses[2], responses[3])
    hr.write()
    list_employees()
    

def delete_employee():
    list_employees()
    number = int(view.get_input("Choose employee to remove(e.g. 1): "))
    hr.delete_employee(hr.HR_DATABASE[number - 1][hr.ID_INDEX])
    hr.write()


def get_oldest_and_youngest():
    hr.read()
    convert_dates = []
    for i in range(len(hr.HR_DATABASE)):
        convert_dates.append(hr.convert_date(hr.HR_DATABASE[i][hr.DOB_INDEX]))
    
    names = (hr.HR_DATABASE[convert_dates.index(min(convert_dates))][1], hr.HR_DATABASE[convert_dates.index(max(convert_dates))][1])
    view.print_general_results(names,"The oldest and the youngest employees are")


def get_average_age():
    hr.read()
    total_age = 0
    for i in range(len(hr.HR_DATABASE)):
        hr.HR_DATABASE[i][hr.DOB_INDEX] = hr.convert_date(hr.HR_DATABASE[i][hr.DOB_INDEX])
        total_age += hr.CURRENT_YEAR - hr.HR_DATABASE[i][hr.DOB_INDEX][0]
    view.print_general_results(total_age/len(hr.HR_DATABASE), "Employees average age is")
    hr.HR_DATABASE.clear()


def next_birthdays():
    hr.read()
    today_date = view.get_input("Today's date (YYYY-MM-DD): ")    
    increased_date = hr.increase_date(today_date)
    today_date = hr.convert_date(today_date)
    birthday_soon = []
    for i in range(len(hr.HR_DATABASE)):
        hr.HR_DATABASE[i][hr.DOB_INDEX] = hr.convert_date(hr.HR_DATABASE[i][hr.DOB_INDEX])
        if hr.HR_DATABASE[i][hr.DOB_INDEX][1] == 1 and hr.HR_DATABASE[i][hr.DOB_INDEX][2] <= 14:
            if today_date[2] - hr.HR_DATABASE[i][hr.DOB_INDEX][2] >= 17:
                birthday_soon.append(hr.HR_DATABASE[i][hr.NAME_INDEX])
        else:
            if [today_date[1], today_date[2]] < [hr.HR_DATABASE[i][hr.DOB_INDEX][1],hr.HR_DATABASE[i][hr.DOB_INDEX][2]] <= [increased_date[1],increased_date[2]]:
                birthday_soon.append(hr.HR_DATABASE[i][hr.NAME_INDEX])
    view.print_general_results(birthday_soon,"Incoming birthdays")
    hr.HR_DATABASE.clear()


def count_employees_with_clearance():
    hr.read()
    employees_with_clearance = 0
    number = int(view.get_input("Enter required clearance level(e.g. 1): "))
    for i in range(len(hr.HR_DATABASE)):
        if int(hr.HR_DATABASE[i][hr.CLEARANCE_INDEX]) <= number:
            employees_with_clearance += 1
    view.print_general_results(employees_with_clearance, "Number of employees with required clearance level")


def count_employees_per_department():
    hr.read()
    emp_per_dep = {}
    for i in range(len(hr.HR_DATABASE)):
        if hr.HR_DATABASE[i][hr.DEPARTMENT_INDEX] in emp_per_dep:            
            emp_per_dep[hr.HR_DATABASE[i][hr.DEPARTMENT_INDEX]] += 1
        else:
            emp_per_dep[hr.HR_DATABASE[i][hr.DEPARTMENT_INDEX]] = 1

    view.print_general_results(emp_per_dep, "Employees per department")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
