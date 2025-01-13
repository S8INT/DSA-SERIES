# sort a list of numbers in ascending order
"""
    - choose pivot element with which to compare
    - partition the array into 2 parts
    - rearrange elements less than the pivot to left
    - elements greater than the pivot to the right
    - recursively sort the elements
    - join the 2 sorted parts using pivot element
    Rerurn : sorted array
"""

def quicksort(nums, start=0, end=None):
    if end is None:
        # nums = list(nums)
        end = len(nums)-1
    
    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)
    return nums

def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums) -1
    # initialize right and left pointers
    left, right = start, end-1
    # iterate through while theyr seperate
    while right > left:
        # increment left pointer if number is less or eqaul to pivot
        if nums[left] <= nums[end]:
            left += 1
        # decrement right pointer if number is greater than pivot
        elif nums[right] > nums[end]:
            right -= 1
        # swap the 2 out 0f place elements
        else:
            nums[left], nums[right] = nums[right], nums[left]
    
    # place the pivot in between the two pointers(parts)
    if nums[left] > nums[end]:
        nums[left], nums[end] = nums[end], nums[left]
        return left
    else:
        return end


l = [1,5,6,2,0,11,3]
pivot = partition(l)
list1 = quicksort(l)
print(list1, pivot) 
  