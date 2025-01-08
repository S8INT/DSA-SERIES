def bubble_sort(nums):
    nums = list(nums)
    for _ in range(len(nums)-1):
        for i in range(len(nums)-1):
            # compare adjacent elements
            if nums[i] > nums[i+1]:
                # swap elements 
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums


lists = [10, 3, 4, 7, 5, 12, 2]
result = bubble_sort(lists)
print(result)

