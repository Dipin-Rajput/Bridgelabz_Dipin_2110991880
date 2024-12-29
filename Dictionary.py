# Dictionary

# Dictionary in python are another datatype.
# It store values in the form of (key : values) pair.
# It is mutable for values, and immutable for keys.
# It is ordered form python version 3.7
# Python dictionaries are essential for efficient data mapping and manipulation in programming.

d = {} # Empty dictionary

# Creation

dictionary = {1 : "name", 2 : "age", 3 : "city"}
print(dictionary)
print(type(dictionary))

# Creating dictionary using dict() constructor

d = dict(name = "Dipin", age = 21, roll_no = 2110991880)
print(d)

# It can have duplicate values, but can't have duplicate keys, if try to write multiple key with same name it will overwrite the values for the same key.

a = {"name" : "mustang", "model" : 455, "year" : 1982, "year" : 2020, "serail_no": 455}
print(a) # {'name': 'mustang', 'model': 455, 'year': 2020, 'serail_no': 455}


# Accessing items

animal = {1 : "dog", 2 : "cat", 3 : "lion", 4 : "elephant"}
print(animal[1]) # Directly access the values using keys within square brackets.

# .get() method

print(animal.get(4))

# The keys() method will return a list of all the keys in the dictionary.

x = animal.keys()
print(x)

animal[5] = "tiger" # Adding new item
print(x)

# The values() method will return a list of all the values in the dictionary.

y = animal.values()
print(y)

# The items() method will return each item in a dictionary, as tuples in a list. 

z = animal.items()
print(z)

# To determine if a specified key is present in a dictionary use the "in" keyword:

if(5 in animal):
    print("yes")


# Adding and Updating dictionary

# update(): The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

car = {"brand" : "audi", "model" : "x5", "color" : "black"}

car["year"] = 2015 # adding new key : value pair
car.update({"number" : "1140"}) 
print(car)

car["color"] = "red" # updating existing key value.
car.update({"model" : "x3"})
print(car)


# Removing items

# pop(): It removes the item with specified key return its value.

rem = car.pop("brand")
print(rem)

# popitem(): It removes the last key-value pair from the dictionary.

key, val = car.popitem()
print(f"key: {key}, value: {val}")

# del(): It removes the specified item with key, also capable of deleting whole structure if nothing passed.

del(car["color"])
print(car)

# clear(): It removes all the item form the dictionary.

car.clear()
print(car)

del(car)
# print(car) # Error: car is not defined.


# Iteration in dictionary

a = {1 : "Dipin", 2 : "Rajput", 3 : 1880}

for i in a:
    print(i) # Printing keys using loop.

for i in a:
    print(a[i]) # Printing values using loop.

for i in a.keys():
    print(i) # Printing keys using .keys() method.

for i in a.values():
    print(i) # Printing values using .values() method.

for i in a.items():
    print(i) # Printing keys and values using .items() method.


# Copy of Dictionary

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
mydict = thisdict.copy()
print(mydict)

# using dict() function

copy = dict(thisdict)
print(copy)


# Nested dictionary

myfamily = { "child1" : {"name" : "Emil", "year" : 2004}, "child2" : {"name" : "Tobias", "year" : 2007}, "child3" : {"name" : "Linus", "year" : 2011}}

print(myfamily["child2"]["name"]) # Accessing items in nested dictionary

for x, obj in myfamily.items(): # looping using .items() method.
  print(x)

  for y in obj:
    print(y + ':', obj[y])



