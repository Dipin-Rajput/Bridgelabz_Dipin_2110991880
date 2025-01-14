# Line Comparison Problem

import math

class Coordinates:

    def __init__(self, x1, y1, x2, y2):

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def length(self):
        l = math.sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)
        return l
    
    def comparison(self, l1, l2):
        if(l1 == l2):
            return "Both lines are equal."
        elif(l1 > l2):
            return "line 1 is greater."
        else:
            return "line 2 is greater."

print("\nEnter Coordinates for line 1.\n")

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

line1 = Coordinates(x1, y1, x2, y2)
l1 = line1.length()

print("\nEnter Coordinates for line 2.\n")

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

line2 = Coordinates(x1, y1, x2, y2)
l2 = line2.length()

result = line1.comparison(l1, l2)

print(f"Length of both lines are {l1} and {l2}")
print("Output is:", result)