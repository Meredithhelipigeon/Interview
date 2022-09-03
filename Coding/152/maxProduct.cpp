// divide and conquer
// Time efficiency: O(nlogn)
// Space efficiency: O(1)
class DC_Solution {
public:
    std::tuple<int, int> find_mami(vector<int>& vi, string order){
        int iteration = -1;
        int i = vi.size() - 1;
        if (order=="R"){
           iteration = 1;
           i = 0;
        } 
        int retValMa = vi[i];
        int retValMi = vi[i];
        int prod = vi[i];
        i += iteration;
        while ((0 <= i) && (i < vi.size())){
            prod *= vi[i];
            retValMa = max(retValMa, prod);
            retValMi = min(retValMi, prod);
            i += iteration;
        }
        return std::make_tuple(retValMi, retValMa);
    }
    
    int divide_and_conquer(vector<int>& cur){
        if (cur.size()==1) return cur[0];
        std::vector<int> left(cur.begin(), cur.begin() + cur.size() / 2);
        std::vector<int> right(cur.begin() + cur.size() / 2, cur.end());
        int leftVal = divide_and_conquer(left);
        int rightVal = divide_and_conquer(right);
        int separate = max(leftVal,rightVal);
        std::tuple<int, int> leftMaMi = find_mami(left, "L");
        std::tuple<int, int> rightMaMi = find_mami(right, "R");
        int combine = max(std::get<0>(leftMaMi)*std::get<0>(rightMaMi), std::get<1>(leftMaMi)*std::get<1>(rightMaMi));
        return max(separate, combine);
    }
    int maxProduct(vector<int>& nums) {
        return divide_and_conquer(nums);
    }
};

// Dynamic Programming
// Time efficiency: O(n)
// Space efficiency: O(n)
class DP_Solution_1 {
public:
    int maxProduct(vector<int>& nums) {
        int dp[nums.size()][2];
        dp[0][0] = nums[0];
        dp[0][1] = nums[0];
        int ret = dp[0][0];
        
        for(int i = 1; i < nums.size(); i++){
            dp[i][0] = min(nums[i],min(nums[i]*dp[i-1][0], nums[i]*dp[i-1][1]));
            dp[i][1] = max(nums[i],max(nums[i]*dp[i-1][0], nums[i]*dp[i-1][1]));
            ret = max(ret, max(dp[i][0],dp[i][1]));
        }
        
        return ret;
    }
};

// Time efficiency: O(n)
// Space efficiency: O(1)
class DP_Solution_2 {
public:
    int maxProduct(vector<int>& nums) {
        int min_so_far = nums[0];
        int max_so_far = nums[0];
        int ret = nums[0];
        
        for(int i = 1; i < nums.size(); i++){
            int last_min_so_far = min_so_far;
            min_so_far = min(nums[i],min(nums[i]*min_so_far, nums[i]*max_so_far));
            max_so_far = max(nums[i],max(nums[i]*last_min_so_far, nums[i]*max_so_far));
            ret = max(max_so_far, ret);
        }
        
        return ret;
    }
};
