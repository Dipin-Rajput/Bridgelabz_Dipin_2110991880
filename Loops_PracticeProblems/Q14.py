# 14) Reverse an integer number.

num = int(input("Enter any number: "))
rev = 0

while(num > 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = int(num / 10)

print("Reverse of the given number is:", rev)