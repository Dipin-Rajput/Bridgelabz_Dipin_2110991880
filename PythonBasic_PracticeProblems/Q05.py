# 5) Check if the first and last numbers of a list are the same: Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.

lst = input("Enter numbers separated by spaces: ").split()

if(lst[0] == lst[-1]):
    print("True, Elements are equal.")
else:
    print("False, Elements are not equual.")
print(lst)