# 15) Get an int value of base raised to the power of exponent: Write a function called exponent(base, exp) that returns an int value of base raised to the power of exp.

def exponent(base, exp):
    return base ** exp

a = int(input("Enter the base number: "))
b = int(input("Enter exponent number: "))

print(exponent(a, b))