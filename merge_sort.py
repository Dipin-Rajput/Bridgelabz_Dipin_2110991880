# Merge Sort

def merge_sort(arr):

    if(len(arr) <= 1):
        return arr
    
    mid = len(arr)//2
    
    l_half = arr[ : mid]
    r_half = arr[mid : ]

    left_half = merge_sort(l_half)
    right_half = merge_sort(r_half)

    return merge(left_half, right_half)

def merge(left, right):

    new = []
    i, j = 0, 0

    while(i < len(left) and j < len(right)):

        if(left[i] < right[j]):
            new.append(left[i])
            i += 1

        else:
            new.append(right[j])
            j += 1

    new.extend(left[i : ])
    new.extend(right[j : ])

    return new

        
my_list = [20, 14, 25, 16, 45, 60, 12, 9]
result = merge_sort(my_list)

print(result)