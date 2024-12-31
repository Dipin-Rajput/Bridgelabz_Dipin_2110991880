# 9) Check Palindrome Number: Write a Python code to check if the given number is a palindrome.

num = int(input("Enter any number: "))

temp = num
rev = 0

while(temp > 0):
    rem = temp % 10
    rev = rem + rev * 10
    temp = int(temp / 10)

if(rev == num):
    print("Yes, it is a Palindrome.")
else:
    print("No, it is not a Palindrome.")