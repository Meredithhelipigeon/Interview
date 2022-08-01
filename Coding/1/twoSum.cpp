class Solution {
public:
    // Solution 1: Time efficiency: O(n^2)
    vector<int> twoSum1(vector<int>& nums, int target) {
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
    
    // Solution 2: Time Efficiency: O(nlogn);
    vector<int> twoSum(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int left = 0;
        int right = nums.size()-1;
        
        while (true){
            if (nums[left]+nums[right]==target){
                vector<int> result;
                result.emplace_back(left);
                result.emplace_back(right);
            } else if (nums[left]+nums[right]<target){
                left += 1;
            } else {
                right -= 1;
            }
        }
    }

    // Solution 3: O(n); Using hashmap
    vector<int> twoSum3(vector<int>& nums, int target) {
        std::map<int,int> unique_numbers;
        vector<int> result;
        for(int i = 0; i < nums.size(); i++){
            if (unique_numbers.find(target-nums[i])!=unique_numbers.end()){
                result.emplace_back(i);
                result.emplace_back(unique_numbers[target-nums[i]]);
                break;
            }
            unique_numbers[nums[i]]=i;
        }
        return result;
    }
};
