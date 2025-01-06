# 9) Find the largest item from a given list: Given a list x = [4, 6, 8, 24, 12, 2], find the largest item.

def largest_num(x):

    max = x[0]

    for i in x:
        if(i > max):
            max = i

    return max

x = [4, 6, 8, 24, 12, 2]

result = largest_num(x)
print("Largest item from given list is:", result)


