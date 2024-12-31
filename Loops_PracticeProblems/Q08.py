# 8) Print list in reverse order using a loop.

lst = [1, 2, 3, 4, 5]
print("List in reverse order:", end = " ")

for i in range(len(lst), 0, -1):
    print(i, end = " ")
