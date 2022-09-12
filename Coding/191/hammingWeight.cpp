// Time efficiency: O(logn)
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ret = 0;
        while (n > 0){
            if (n%2==1) ret += 1;
            n /= 2;
        }
        return ret;
    }
};

// Bit operations:
// Time efficiency: O(log n)
class Solution_Bit {
public:
    int hammingWeight(uint32_t n) {
        int ret = 0;
        int mask = 1;
        while (n > 0){
            if (n & mask == 1) ret += 1;
            n = n >> 1;
        }
        return ret;
    }
};

// Bit Manipulation
// Time efficiency: O(log (number of 1))
class Solution_Bit_Manipulation {
public:
    int hammingWeight(uint32_t n) {
        int ret = 0;
        while (n!=0) {
            ret += 1;
            n &= n - 1;
        }
        return ret;
    }
};
