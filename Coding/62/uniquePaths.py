from math import comb
class Solution:
    # Solution 1: mathematics way
    def uniquePaths1(self, m: int, n: int) -> int:
        return comb(m+n-2,n-1)

    # Solution 2: mathematics way
    # Time efficiency: Peter Borwein: O((m+n)(log(m+n))loglog(m+n))
    def uniquePaths2(self, m: int, n: int) -> int:
        def nCr(i,j):
            if i==j:
                return 1
            elif j==1:
                return i
            else:
                return nCr(i-1,j)+nCr(i-1,j-1)
        return nCr(m+n-2,m-1)
    
    # Solution 3: DP Version
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for i in range(m)]
        
        # initialization
        for i in range(m):
            dp[i][0]=1
        for j in range(n):
            dp[0][j]=1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]

        return dp[-1][-1]
