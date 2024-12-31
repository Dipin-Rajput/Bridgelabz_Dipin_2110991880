# 11) Get each digit from a number in the reverse order: For example, if the given integer number is 7536, the output shall be "6 3 5 7".

num = 7536
temp = num

while(temp > 0):

    rem = temp % 10
    print(rem, end = " ")
    temp = int(temp / 10)
