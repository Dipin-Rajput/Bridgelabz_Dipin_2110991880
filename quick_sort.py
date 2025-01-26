# Quick Sort

def quick_sort(arr, low, high):
    
    if(low < high):
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

    return arr

def partition(arr, low, high):

    p = arr[low]
    i = low + 1
    j = high

    while(True):
        while(i <= j and arr[i] <= p):
            i += 1

        while(i <= j and arr[j] >= p):
            j -= 1

        if(i <= j):
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]

    return j

my_list = [20, 14, 25, 16, 45, 60, 12, 9]
result = quick_sort(my_list, 0, len(my_list) - 1)

print(result)