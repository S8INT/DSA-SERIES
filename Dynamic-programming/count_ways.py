
"""
# frog jumps either 1, 2, or 3 steps to reach the top.
# how many ways can it take to reach top of the nth step
"""

def count_ways(n, memo):
    """
    Base case:
    - if n is o there is only 1 way.
    - if n is less than 0 to zero return 0
    ways: is equal to the sum of all possible ways called recursively
    and stored in memo={}, using the memoization method
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif n in memo:
        return memo[n]
    else:
        memo[n] = count_ways(n-1, memo) + count_ways(n-2, memo) + count_ways(n-3, memo)
        return memo[n]
