class Solution:
    # Solution 1: DP; dp[i][j] means that the number of patterns that have j inverse pairs when we only change the order from [:i+1]
    # Time efficiency: O(n*n*k)
    # Space efficiency: O(n*k)
    def kInversePairs1(self, n: int, k: int) -> int:
        M = 10**9+7
        dp = [[0]*(k+1) for i in range(n)]
        
        # Initialization
        for i in range(n):
            dp[i][0]=1
        
        # Update the DP
        for i in range(1,n):
            for inverseNum in range(1,k+1):
                startIndex=inverseNum-i
                dp[i][inverseNum]=sum(dp[i-1][max(0,startIndex):inverseNum+1])
    
        return dp[-1][-1]

    # Solution 2: DP with optimization; Don't need to calculate the sum every time;
    # Time efficiency: O(n*k)
    # Space efficiency: O(n*k)
    def kInversePairs2(self, n: int, k: int) -> int:
        M = 10**9+7
        dp = [[1]+[0]*(k) for i in range(n)]
        
        # Update the DP
        for i in range(1,n):
            cur=dp[i-1][0]
            for inverseNum in range(1,k+1):
                startIndex=inverseNum-i
                if startIndex-1>=0:
                    cur-=dp[i-1][startIndex-1]
                cur+=dp[i-1][inverseNum]
                dp[i][inverseNum]=cur%M
        return dp[-1][-1]
