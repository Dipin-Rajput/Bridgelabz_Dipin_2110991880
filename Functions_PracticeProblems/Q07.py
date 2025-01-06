# 7) Assign a different name to function and call it through the new name: Below is the function display_student(name, age). Assign a new name show_student(name, age) to it and call it using the new name.

def display_student(name, age):
    print(f"Name is: {name}\nAge is: {age}")

display_student("John", 25)

show_student = display_student

show_student("Carl", 23)