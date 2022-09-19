// Pretty intuitive solution: O(nlogn)
class Solution1 {
public:
    vector<int> countBits(int n) {
        vector<int> ret;
        int mask = 1;
        for(int i = 0; i < n+1; i++){
            int cur = i;
            int numsOfOnes = 0;
            while(cur!=0){
                if ((cur&mask)==1){
                    numsOfOnes += 1;
                }
                cur = cur >> 1;
            }
            ret.emplace_back(numsOfOnes);
        }
        return ret;
    }
};

// Use DP to solve the problem: O(n)
class Solution2 {
public:
    vector<int> countBits(int n) {
        vector<int> ret(n+1,0);
        int b = 1;
        int add_on = 0;
        
        while (b+add_on <= n){
            while ((add_on < b) && (b+add_on <= n)){
                ret[b+add_on] = ret[add_on] + 1;
                add_on += 1;
            }
            b <<= 1;
            add_on = 0;
        }
        return ret;
    }
};
