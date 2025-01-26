# Binary Search

def binary_search(arr, low, high, target):

    while(low <= high):

        middle = int((low + high)/2)

        if(arr[middle] == target):
            return f"Element found at {middle} index.\n"
        
        elif(target > arr[middle]):
            low = middle + 1

        else:
            high = middle - 1

    return "Element not found.\n"

my_list = [20, 14, 25, 16, 45, 60, 12, 9]
target = int(input("\nEnter the number you want to search: "))

my_list.sort()

result = binary_search(my_list, 0, len(my_list)-1, target)
print(result)