# 4) Create a function with a default argument: Write a program to create a function show_employee() using the following conditions. It should accept the employee’s name and salary and display both. If the salary is missing in the function call then assign default value 9000 to salary.

def show_employee(name, salary = 9000):
    print(f"Employee name: {name}\nEmployee slaray: {salary}")

name = input("Enter your name: ")
salary = input("Enter your salary (press Enter to skip): ")

if (salary.strip() == ""):
    show_employee(name)
else:
    salary_input = int(salary)
    show_employee(name, salary_input)
