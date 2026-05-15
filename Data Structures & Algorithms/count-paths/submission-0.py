class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #brute force
        twoD_arr = [[0]*n]*m
        for i in range(m):
            twoD_arr[i][0] = 1
        for j in range(n):
            twoD_arr[0][j] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                twoD_arr[i][j] = twoD_arr[i][j-1] + twoD_arr[i-1][j]
        return twoD_arr[m-1][n-1]