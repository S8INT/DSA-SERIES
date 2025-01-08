def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns - a new sorted list
    Divide: find the midpoint of the list and divides into sublist
    conquer: Recursively sort the sublist created in prev step
    combine: Merge the sorted sublist created in prev step
    """
    if len(list)<=1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)

def split(list):
    """
    divide the un sorted list at midpoint into sub-lists
    Returns two sub-lists left and right
    Takes O(n) time complete the run process.

    """
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    return left, right

def merge(left, right):
    """
    merges 2 lists
    returns a new merged list
    """
    l =[]
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1
    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1
    return l

alist = [54, 22, 62, 10, 65, 80, 57, 30]
l = merge_sort(alist)
print(l)