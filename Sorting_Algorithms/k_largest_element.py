"""
# given an array of positive integers and an integer k,
# return k largest elements in decreasing order
# input: arr = [70, 10, 30, 20, 40, 50, 60], k = 3
# output: [70, 60, 50]
"""
# using quick sort
# select a pivot element
# partition the array into two sub-arrays
# elements less than the pivot and elements greater than the pivot
# recursively sort the sub-arrays
# return the k largest elements in decreasing


def k_largest_element(arr, k):
    """
    function finds the k largest elements in array
    k = number of largest elements to return
    - sorts them in decreasing order
    - Returns the k largest elements
       
    """
    if len(arr) <= 1:
        return arr
    
    n = len(arr)
    pivot = arr[n//2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    if k < len(right):
        return k_largest_element(right, k)
    elif k < len(right) + len(equal):
        return right + equal
    else:
        return right + equal + k_largest_element(left, k - len(right) - len(equal))

