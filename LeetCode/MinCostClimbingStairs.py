def minCostClimbingStairs(cost):
    if len(cost) == 0:
        return 0
    elif len(cost) == 1:
        return cost[0]
    elif len(cost) == 2:
        return min(cost[0], cost[1])
    else:
        dp = [0 for i in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[-1], dp[-2])


print("cost is:", minCostClimbingStairs([10, 15, 20]))
print("cost is:", minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

# [10, 15, ]
