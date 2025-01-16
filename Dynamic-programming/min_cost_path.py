# program finds the minimum cost path from (0,0) to
# (m,n), given 2d cost matrix. using memoization

def minCost(cost, m, n, memo):
    # if indices are out of bounds return largeValue
    if m<0 or n<0:
        return float('inf')
    # base case
    if m ==0 or n==0:
        return cost[m][n]
    # retun calculated value
    if memo[m][n] != -1:
        return memo[m][n]

    # store calculated results
    memo[m][n] = cost[m][n] + min(
        minCost(cost, m, n-1, memo),
        minCost(cost, m-1, n, memo),
        minCost(cost, m-1, n-1, memo)
        )
    return memo[m][n]
