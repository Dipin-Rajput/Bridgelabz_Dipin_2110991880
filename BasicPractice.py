# Conditional Statements: if - elif - else

# 1. WAP to check if a number entered by the user is odd or even.

a = int(input("Enter any number: "))

if(a % 2 == 0):
    print("It is an even number.")
else:
    print("It is an odd number.")
print()


# 2. WAP to find the greatest of 3 numbers entered by the user.

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if(x >= y and x >= z):
    print("Greatest number is:", x)
elif(y >= x and y >= z):
    print("Greatest number is: ", y)
else:
    print("Greatest number is:", z)
print()


# 3. WAP to check if a number is a multiple of 7 or not

b = int(input("Enter any number: "))

if(b % 7 == 0): 
    print("It is the multiple of 7.")
else:
    print("It is not the multiple of 7.")
print()


# Nested if

age = 28

if(age >= 18):
    if(age <= 24):
        print("Eligible for Job.")
    else:
        print("Not eligible for Job")
else:
    print("Under age")


# Loops

# 1. WAP to print the square of first 10 numbers.

i = 1

while(i <= 10):
    print(i * i)
    i+=1

# for loop with break and continue

# break statement breaks the loop when the condition is met.
# continue statement skip the iteration when the condition is met.

str = "DipinRajput"

for i in str:
    if(i == "a"):
        break
    else:
        print(i)
print()

for i in str:
    if(i == "i"):
        continue
    else:
        print(i)
print()
