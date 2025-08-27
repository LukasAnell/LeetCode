from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        totalCost = 0
        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                totalCost += cost[i]
        return totalCost
