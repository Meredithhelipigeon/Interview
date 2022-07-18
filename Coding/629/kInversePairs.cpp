class Solution {
public:
    int kInversePairs(int n, int k) {
        int DP[n][k+1];
        memset(DP,0,sizeof(DP));
        int M = pow(10,9)+7;
        for(int i = 0; i < n; i++){
            DP[i][0]=1;
        }
        
        for(int i = 1; i < n; i++){
            int cur = 1;
            int startIndex=-1;
            for(int j = 1; j < k+1; j++){
                startIndex=j-i;
                if (startIndex-1>=0) cur-=DP[i-1][startIndex-1];
                cur+=DP[i-1][j];
                cur=(cur % M + M) % M;
                DP[i][j]=cur;
            }
        }
        return DP[n-1][k];
    }
};
