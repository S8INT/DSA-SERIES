""" 
function finds the minimum number of swaps required to sort 
an array of distinct elements in ascending order
- input: arr = [7, 1, 3, 2, 4, 5, 6]
- output: 5
"""

# using bubble sort technique;
# pass element and compare it to adjacent element
# swap element if its greater than the adjacent element
# increment the count of swaps
# repeat the process until the array is sorted
# return the count of swaps

"""
def minimum_swaps(arr):
    count = 0

    for i in range(len(arr)-1):
        swapped = False
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                count += 1
        if not swapped:
            break
    return count

n  = minimum_swaps([7, 1, 3, 5, 6])
print(n)
"""

# using hash table
# create a hash table with the index of each element
# sort the array
# iterate through the array
# if the element is not in the correct position
# swap the element with the element at the correct position
# update the hash table
# increment the count of swaps  
# return the count of swaps

def minimum_swaps(arr):
    count = 0
    hash_table = {val: i for i, val in enumerate(arr)}
    sorted_arr = sorted(arr)

    for i in range(len(arr)):
        # check if element is the correct position
        if arr[i] != sorted_arr[i]:
            correct_index = hash_table[sorted_arr[i]]
            # swap the element with the element at the correct position
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
            hash_table[arr[correct_index]] = correct_index
            count += 1
    return count

n  = minimum_swaps([7, 1, 3, 2, 4, 5, 6])
print(n)
