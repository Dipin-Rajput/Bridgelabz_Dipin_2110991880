# 5) Create an inner function to calculate the addition in the following way: Create an outer function that will accept two parameters, a and b. Create an inner function inside an outer function that will calculate the addition of a and b. At last, an outer function will add 5 into addition and return it.

def outer(a, b):

    def inner(a, b):
        return a + b
    
    sum = inner(a, b)
    return sum + 5

first_num = 45
second_num = 55

print(f"Sum of two numbers with +5 addition is: {outer(first_num, second_num)}")