employees ={101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}}
#function for add employee
def add_employees():
    while True:
        emp_id = int(input('Enter employee id: '))
        if emp_id in employees:
            print('This employee already exists\n please choose another one')
        else:
            break

    name = input('Enter employee name: ')
    age = int(input('Enter employee age: '))
    department = input('Enter employee department: ')
    salary = int(input('Enter employee salary: '))

    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }
    print("employee added successfully")
 # function for view the employee
def view_employees():
    if not employees:
        print("no employees exist\n")
        return

    print("\nID\tName\tAge\tDepartment\tSalary")
    print("-"*50)
    for emp_id, details in employees .items():
        print(emp_id, "\t", details['name'], "\t", details['age'], "\t", details['department'])
        print()
# function for search employees
        def search_employees():
            emp_id = int(input('Enter employee id: '))

            if emp_id in employees:
                emp = employees[emp_id]
                print("\nEmployee Found:")
                print("Name: ", emp['name'])
                print("Age: ", emp['age'])
                print("Department: ", emp['department'])
                print("Salary: ", emp['salary'], "\n")
            else:
                print("Employee not found.\n")
# function for main menu
def main_menu():
    while True:
        print("Employee Management system")
        print("1. View employees")
        print("2. Add employee")
        print("3. search_employee")
        print("4. exit\n")

        choice = int(input('Enter your choice: '))

        if choice == 1:
            view_employees()

        if choice == 2:
            add_employees()

        if choice == 3:
            search_employee()

        if choice == 4:
            print("Thank you for using this program")

        else:
            print("you have choosen wrong option")






