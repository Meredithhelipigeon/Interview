class Solution {
public:
    // Time efficiency: O(m+n), Space efficiency: O(1)
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        
        int i = 0;
        int j = matrix[0].size()-1;
        
        while (i<m && j>=0){
            if (matrix[i][j] == target){
                return true;
            } else if (matrix[i][j] < target){
                i+=1;
            } else {
                j-=1;
            }
        }
        return false;
    }

    // Time efficiency: O(mlogn), Space efficiency: O(1)
    bool searchMatrix2(vector<vector<int>>& matrix, int target) {
        for(int i = 0; i < matrix.size(); i++){
            int left = 0;
            int right = matrix[0].size()-1;
            while (left <= right) {
                int mid = (right+left)/2;
                if (matrix[i][mid]==target){
                    return true;
                } else if (matrix[i][mid] > target){
                    right = mid-1;
                } else {
                    left = mid+1;
                }
            }
        }
        return false;
    }
};
