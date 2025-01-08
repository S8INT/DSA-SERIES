""" A list of numbers obtained by rotating a sorted list in an unknown number
of times. write a function to determine the minimun number of times the
original list was rotated to to obtain the given list.
- expected worst-case complexity O(log n)
- assume all numbers in the list are unique
"""
# function to count min number of rotations
# check if list is empty
# if it has one element cant be sorted
# determine the minimum number of rotations
# retrun number of rotations

def countRotations(times):
	n = len(list)
	left, right = n+1, n-1
	while n > 0:
		pass