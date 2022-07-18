class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ret;
        for(int i = 0; i < nums.size();i++){
            for(int j = i+1; j < nums.size(); j++){
                if (nums[i]+nums[j]==target){
                    ret.emplace_back(i);
                    ret.emplace_back(j);
                    break;
                }
            }
        }
        return ret;
    }
};
