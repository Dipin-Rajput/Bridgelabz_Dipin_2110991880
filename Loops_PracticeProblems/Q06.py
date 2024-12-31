# 6) Count the total number of digits in a number.

num = int(input("Enter any number: "))
count = 0

if(num != 0):

    while(num > 0):
        count+=1
        num = int(num/10)
    print("Total number of digits in given number is:", count)

else:
    print("Total number of digits in given number is:", 1)

