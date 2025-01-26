# Linear Search

def linear_search(arr, target):

    for i in range(len(arr)):
        if(arr[i] == target):
            return f"Number found at {i} index.\n"
        
    return "Number not found.\n"
        

my_list = [20, 14, 25, 16, 45, 60, 12, 9]
target = int(input("\nEnter the number you want to search: "))

result = linear_search(my_list, target)
print(result)