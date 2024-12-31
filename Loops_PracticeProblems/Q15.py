# 15) Print elements from a given list present at odd index positions.

lst = [1, 8, 7, 9, 10, 5, 6, 33, 45, 7]
odd_position = []

for i in range(len(lst)):
    if(i % 2 != 0):
        odd_position.append(lst[i])

print("Elements present at odd index positions:", odd_position)
