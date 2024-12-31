# 7) Print the following pattern:

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

n = int(input("Enter number of rows you want in pattern: "))

for i in range(n):
    for j in range(n-i, 0, -1):
        print(j, end = " ")
    print()

