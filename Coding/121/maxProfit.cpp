class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int first = prices[0];
        int ret = 0;
        for(auto p: prices){
            if (p < first) first = p;
            else ret = max(ret, p-first);
        }
        return ret;
    }
};
