class Solution:
    def climbStairs(self, n: int) -> int:
        #Tabulation Method
        if n==1: return 1
        if n==2: return 2
        map = {1:1,2:2}
        for i in range(3,n+1):
            map[i] = map[i-1]+map[i-2]
        return map[n]