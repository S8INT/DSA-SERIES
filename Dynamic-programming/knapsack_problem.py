"""
Given N items where each item has some weight and profit associated with it
 and also given a bag with capacity W, [i.e., the bag can hold at most W weight in it].
 The task is to put the items into the bag such that
 the sum of profits associated with them is the maximum possible.
"""

# function builds a dp[][] in a tabulation manner
# returns the maximum value that can be put in the knapsack of capacity W.

def knapSack(capacity, weight, val):
    n = len(weight)
    dp = [[0 for x in range(capacity + 1)][for x in range(n+1)]

    # build the dp[][] in bottom-up format
    for i in range(n+1):
        for c in range(capacity + 1):
          if i ==0 or c ==0:
              dp[i][c] = 0
          elif weight[i -1] <= c:
               dp[i][c] = max(val[i-1] + dp[i-1][c- weight][i-1], dp[i-1][c])
          else:
              dp[i][c] = dp[i -1][c]
    return dp[n][capacity]
