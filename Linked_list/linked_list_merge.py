from linked_list import Linkedlist

def merge_sort(linked_list):
    """
    sort is linked in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list
    """
    if linked_list.size() ==1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """divide the unsorted list"""
    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2
        mid_node = linked_list.node_at_index(mid -1)

        left_half = linked_list
        right_half = Linkedlist()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half

def merge(left, right):
    """
    Merges 2 linked lists , sorting data in nodes
    Returns a node, merged list
    """

    # create a new linked list that contains nodes from
    # merging left and right
    merged =  Linkedlist()

    # add a fake list that will be discarded later
    merged.add(0)
    # set current to the head of the linked list
    current = merged.head
    # fetch
    left_head = left.head
    right_head = right.head

    # iterate left and right until we reach the tail node
    while left_head or right_head:
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        # if the head node of right is None , we wre past the tail
        # add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            # not at either tail node
            left_data = left_head.data
            right_data = right_head.data
            if left_data < right_data:
                current.next_node = left_head
                # move left head to next node
                left_head = left_head.next_node
            # if data on left is greater than right, set current to right node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        # move current to next node
        current = current.next_node

    # discard fake head
    head = merged.head.next_node
    merged.head = head

    return merged

l = Linkedlist()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)
print(l)