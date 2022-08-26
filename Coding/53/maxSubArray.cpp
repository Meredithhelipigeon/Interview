class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int remain = 0;
        int left = 0;
        int ret = std::numeric_limits<int>::min();
        for(int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            ret = max(ret, remain+num);
            remain += num;
            while (remain < 0 && left <= i) {
                remain -= nums[left];
                left +=1;
            }
        }
        return ret;
    }
};
