# Bubble Sort

def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if(arr[j] > arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr

my_list = [20, 14, 25, 16, 45, 60, 12, 9]
result = bubble_sort(my_list)

print(result)