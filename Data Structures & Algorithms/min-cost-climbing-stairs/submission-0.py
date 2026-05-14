class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==1: return cost[0]
        prev, cur = cost[0], cost[1]
        for i in range(2, len(cost)):
            prev, cur = cur, min(prev, cur)+cost[i]
        return min(prev, cur)