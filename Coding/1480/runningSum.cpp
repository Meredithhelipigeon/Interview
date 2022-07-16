class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int cur = 0;
        std::vector<int> v;
        for (auto n: nums) {
            cur +=n ;
            v.push_back(cur);
        }
        return v;
    }
};
