class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int nums_sum = 0;
        for(int i = 0; i <= nums.size(); i++){
            nums_sum += i;
        }
        for(auto n: nums){
            nums_sum -= n;
        }
        return nums_sum;
    }
};

// XOR cancellation: O(n)
class Solution2 {
public:
    int missingNumber(vector<int>& nums) {
        int missing_num = nums.size();
        for(int i = 0; i < nums.size(); ++i){
            missing_num ^= i ^ nums[i];
        }
        return missing_num;
    }
};
