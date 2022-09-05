// Time efficiency: O(n^2)
class Solution1 {
public:
    vector<int> nums_global;
    vector<vector<int>> twoSum(int start, int target){
        std::set<int> unique_record = {};
        std::set<int> findSet;
        vector<vector<int>> ret;
        for(int i = start; i < nums_global.size(); ++i){
            if (unique_record.find(target - nums_global[i]) != unique_record.end() && 
                findSet.find(nums_global[i]) == findSet.end()){
                std::vector<int> cur;
                cur.emplace_back(nums_global[i]);
                cur.emplace_back(target - nums_global[i]);
                ret.emplace_back(cur);
                findSet.insert(target - nums_global[i]);
                findSet.insert(nums_global[i]);
            }
            unique_record.insert(nums_global[i]);
        }
        return ret;
    }
    
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        nums_global = nums;
        vector<vector<int>> result;
        for(int i = 0; i < nums.size(); ++i){
            if (i == 0 || nums[i] != nums[i-1]) {
                vector<vector<int>> ret = twoSum(i+1,-nums[i]);
                if (ret.size() > 0) {
                    for(auto r: ret){
                        r.emplace_back(nums[i]);
                        result.emplace_back(r);
                    }
                }
            }
        }
        return result;
    }
};

// Time efficiency: O(n^2)
class Solution2 {
public:
    void twoSum(vector<int>& nums, int start, vector<vector<int>> &res){
        int left = start + 1;
        int right = nums.size()-1;
        while (left < right) {
            int curSum = nums[left] + nums[right] + nums[start];
            if(curSum == 0){
                res.push_back({nums[left],  nums[right], nums[start]});
                left += 1;
                right -= 1;
                while (left < right && nums[left] == nums[left-1]){
                    left += 1;
                }
            } else if (curSum > 0) {
                right -= 1;
            } else {
                left += 1;
            }
        }
        return;
    }
    
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        for(int i = 0; i < nums.size(); ++i){
            if (i == 0 || nums[i] != nums[i-1]) {
                twoSum(nums, i, result);
            }
        }
        return result;
    }
};
