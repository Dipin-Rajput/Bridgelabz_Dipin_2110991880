# Else with Loops

# else statement at the end of the loop will executes after the loop is completed.

i = 0
while(i <= 10):
    print(i)
    i+=1
else:
    print("Loop Ended")

# But with the break statement, it breaks the loop and else is not going to execute.

i = 0
while(i <= 10):
    if(i == 5):
        break
    print(i)
    i+=1
else:
    print("Loop Ended")

# It is going to work with the continue statement, as continue statement completes the loop.

i = 0
while(i <= 10):
    if(i == 5):
        i+=1
        continue
    print(i)
    i+=1
else:
    print("Loop Ended")

# Printing even and odd number using continue statement

i = 0
while(i <= 10):
    if(i % 2 == 0):
        i+=1
        continue
    print(i)
    i+=1
else:
    print()

i = 0
while(i <= 10):
    if(i % 2 != 0):
        i+=1
        continue
    print(i)
    i+=1
else:
    print()

# Range Function

# Range function return a sequence of numbers, statring from 0 (by default), and increment by 1 (by default), and stops before a specified number.
# range(start, stop, step)

print(range(5)) # It will the just print the range function range(0, 5)

seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print()

# or

for i in seq:
    print(i)

for i in range(10): # Providing only stop value, by default starts form 0.
    print(i)
print()

for i in range(5, 10): # Providing both start = 5 and stop = 10.
    print(i)
print()

for i in range(2, 10, 2): # Providing all three values starting with 2, stopping at 9, and increment by 2.
    print(i)

# Basic Programs Based on for and range

## Print Number form 1 to 100

for i in range(1, 101):
    print(i)

# Print Number from 100 to 1

for i in range(100, 0, -1):
    print(i)

# Print the multiplication table of a number n.

n = int(input("Enter any number: "))

for i in range(11):
    print(n, "X", i, "=", n*i)

# Pass

# Pass is a null statement that does nothing, It is used as a placeholder for future code.

# for i in range(5):
# print("This is the after statement.") # This statement will result in Indentation error, It will expect the next line in the for statement.

# To avoid these kind of scenarios we use pass statement and if we want to write the code for future in that statement.

for i in range(5):
    pass
print("This is the after statement.")

# It can also be used with if statements.

if(i > 5):
    pass

# Basic Problems

# WAP to find the sum of first n numbers.

n = int(input("Enter any number: "))

i = 1
sum = 0
while(i <= n):
    sum += i
    i+=1
print("Sum of first n numbers is:", sum)

# WAP to find the factorial of first n numbers.

x = int(input("Enter any number: "))
fact = 1

for i in range(x, 0, -1):
    fact = fact * i
print("Factorial:", fact)

# Match Case

def num_check(x):
    match x:
        case 10 | 20 | 30:  # Matches 10, 20, or 30
            print(f"Matched: {x}")
        case 10:
            print("Another match for:", x) # It will break as soon as the first match found.
        case _:
            print("No match found") # Default case

num_check(10)
num_check(20)
num_check(25)

# Match Case with if statement

def num_check(x):
    match x:
        case 10 if x % 2 != 0:  # Match 10 only if condition is True.
            print("Matched 10 and it's even!")
        case 10:
            print("Matched 10, but it's not even.")
        case _:
            print("No match found") # Default case

num_check(10)
num_check(15)