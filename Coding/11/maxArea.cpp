// Time Complexity: O(n)
// Space Complexity: O(1)
// Greedy Algorithm
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size()-1;
        int ret = 0;
        while (left < right){
            int curArea = min(height[left], height[right]) * (right - left);
            ret = max(curArea, ret);
            if (height[left] > height[right]) right -=1;
            else left += 1;
        }
        return ret;
    }
};
