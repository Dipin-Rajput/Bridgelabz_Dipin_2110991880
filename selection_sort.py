# Selection Sort

def selection_sort(arr):

    for i in range(len(arr)):
        min_val = i
        for j in range(i + 1, len(arr)):
            if(arr[j] < arr[min_val]):
                min_val = j

        temp = arr[i]
        arr[i] = arr[min_val]
        arr[min_val] = temp

    return arr

my_list = [20, 14, 25, 16, 45, 60, 12, 9]
result = selection_sort(my_list)

print(result)