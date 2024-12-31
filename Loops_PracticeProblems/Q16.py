# 16) Calculate the cube of all numbers from 1 to a given number.

num = int(input("Enter any number: "))
cube = []

for i in range(1, num + 1):
    cube.append(i**3)

print("Cube of all numbers upto given number:", cube)