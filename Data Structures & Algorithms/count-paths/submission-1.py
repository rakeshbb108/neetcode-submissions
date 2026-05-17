class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #space optimized
        dp = [1]*n
        for rows in range(1,m):
            for i in range(1,n):
                dp[i] = dp[i]+dp[i-1]
        return dp[n-1]
