# recursive function to find the mini cost path from (0,0)
# to (m,n)of a cost matrix

def miniCost(cost, m, n):
    """
     Check if indices are out of bound and return large value
     Base case: cells start at cost[0][0]
     Determine: the mincost by recursively calculating the
     total cost through all possible paths
     """
    if m < 0 or n < 0:
        return float('inf')

    # base case, initial cell
    if m ==0 or n ==0:
        return cost[m][n]

    return cost[m][n] + min(
        miniCost(cost, m, n-1),
        miniCost(cost, m-1, n),
        miniCost(cost, m-1, n-1)
    )
