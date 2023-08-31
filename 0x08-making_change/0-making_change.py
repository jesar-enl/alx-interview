#!/usr/bin/python3
"""
Python implementation of the makeChange function
"""

def makeChange(coins, total):
    """Making change function"""
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins needed for each value from 1 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1  # Cannot make the total with the given coins
    else:
        return dp[total]
