class Solution {
public:
    int fib(int n) {
        int last = 1;
        int second_last = 0;
        int cur = 0;
        
        // base case
        if (n==0) {
            return 0;
        } else if (n==1) {
            return 1;
        }
        
        // iteration
        for(int i = 2;i<=n;i++){
            cur = last + second_last;
            second_last = last;
            last = cur;
        }
        
        return cur;
    }
};
