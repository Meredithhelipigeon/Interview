class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int>left(nums.size(), 1);
        vector<int>right(nums.size(), 1);
        int l = 1;
        int r = 1;
        
        for(int i = 0; i < nums.size(); ++i){
            l *= nums[i];
            left[i] = l;
            r *= nums[nums.size() - i - 1];
            right[nums.size() - i - 1] = r;
        }
        
        vector<int> ret(nums.size(), 1);
        if (nums.size()==1) return ret;
        ret[0] = right[1];
        ret[nums.size()-1] = left[nums.size()-2];
        for(int i = 1; i < nums.size()-1; ++i){
            ret[i] = left[i-1]*right[i+1];
        }
        
        return ret;
    }
};
