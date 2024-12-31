# 17) Find the sum of the series up to n terms.

n = int(input("Enter any number: "))
sum = 0

for i in range(n+1):
    sum += i

print("Sum of the series upto n terms:", sum)