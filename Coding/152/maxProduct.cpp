// divide and conquer
class Solution1 {
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
