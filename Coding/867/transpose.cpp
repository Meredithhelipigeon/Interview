class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        vector<vector<int>> ret;
        for(int i = 0; i < matrix[0].size();i++){
            vector<int> v;
            for(int j = 0; j<matrix.size();j++){
                v.emplace_back(matrix[j][i]);
            }
            ret.emplace_back(v);
        }
        return ret;
    }
};
