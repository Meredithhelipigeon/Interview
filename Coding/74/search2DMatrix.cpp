class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        int start = 0;
        int end = m*n-1;

        while (start <= end) {
            int mid = (start + end) / 2;
            int mid_value = matrix[mid/n][mid%n];

            if (mid_value == target){
                return true;
            } else if (mid_value < target){
                start = mid+1;
            } else {
                end = mid-1;
            }
        }

        return false;
    }
};
