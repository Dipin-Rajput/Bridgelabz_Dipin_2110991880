# 18) Print the following pattern:

# * * * * *
# * * * *
# * * *
# * *
# *

n = int(input("Enter number of rows you want in pattern: "))

for i in range(n):
    for j in range(n-i):
        print("*", end = " ")
    print()
