# 10) Calculate the sum and average of the digits present in a string.

# Given: str1 = "PYnative29@#8496"

# Expected Outcome:

# Sum is: 38
# Average is: 6.333333333333333

str1 = "PYnative29@#8496"
sum, count = 0, 0

for i in str1:
    if(i.isdigit()):
        sum = sum + int(i)
        count += 1

avg = sum / count

print(f"Sum is: {sum}\nAverage is: {avg}")