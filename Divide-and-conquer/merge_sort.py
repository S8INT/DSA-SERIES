# write a function to sort a list of notebooks in decreasing order of likes.
def merge_sort(nums):
    # terminating condition; if list is empty or has 1 element
    if len(nums) <= 1:
        return nums
    # find the midpoint
    mid = len(nums)//2
    # split the list into 2 halves
    left = nums[:mid]
    right = nums[mid:]
    # sort each side recursively
    left_sort, right_sort = merge_sort(left), merge_sort(right)
    # combine the two sorted halves
    sorted_nums = merge(left_sort, right_sort)
    return sorted_nums

def merge(nums1, nums2):
    merged = []
    # set 2 iteration values
    i, j = 0, 0
    # loop over the 2 lists
    while i < len(nums1) and j < len(nums2):
        # add the smaller element in the result and move to next element
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    # get remaining elements
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]

    # Return the final merged array
    return merged + nums1_tail + nums2_tail

