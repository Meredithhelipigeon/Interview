class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        if (arr.size()<1){
            return true;
        }
        
        int gap = arr[1]-arr[0];
        for(int i = 1; i < arr.size(); i++){
            if (arr[i]-arr[i-1]!=gap){
                return false;
            }
        }
        return true;
    }
};
