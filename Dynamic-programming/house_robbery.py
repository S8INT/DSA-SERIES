# program finds the maximum amount of money that
# can be robbed from non adjacent houses

def maxRobbery(homeValue):
    """
    dp[]: stores the maximum robbery at each house
    Base cases:
      - wen dp[0] is equal to 0
      - wen dp[1] equals house value[0]
    Fill the dp array using bootom-up method
    Return: maximum ammount robbed
    """
    n = len(homeValue)
    dp = [0] * (n + 1)

    # base cases, initialization
    dp[0] = 0
    dp[1] = homeValue[0]

    for i in range(2, n + 1):
        dp[i] = max(homeValue[i -1]+ dp[i -2], dp[i-1])
    return dp[n]
