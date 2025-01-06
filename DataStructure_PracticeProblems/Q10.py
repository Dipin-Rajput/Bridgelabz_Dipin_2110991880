# 10) Remove duplicates from a list and create a tuple and find the minimum and maximum number.

# Given:
# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

# Expected Outcome:

# unique items [87, 45, 41, 65, 99]
# tuple (87, 45, 41, 65, 99)
# min: 41
# max: 99

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
tup = ()

for i in sample_list:
    if(i not in tup):
        tup = tup + (i,)

max = tup[0]
min = tup[0]

for i in tup:
    if(i > max):
        max = i
    if(i < min):
        min = i

print("Unique item in tuple is:", tup)
print("Maximum element:", max)
print("Minimum element:", min)