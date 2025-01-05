# 15) Remove empty strings from a list of strings.

# Given: str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

# Expected Output:

# Original list of strings: ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']
# After removing empty strings: ['Emma', 'Jon', 'Kelly', 'Eric']

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
new_list = []

print("Original list of strings:", str_list)

for i in str_list:

    if(i):
        new_list.append(i)

print("After removing empty strings:", new_list)