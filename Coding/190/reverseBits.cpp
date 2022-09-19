// Both Solution1 and Solution2 are Bit by Bit
class Solution1 {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t ret = 0;
        uint32_t cur = pow(2,31);
        int mask = 1;
        
        while (n>0){
            ret += cur * (n&mask);
            cur >>= 1;
            n >>= 1;
        }
        return ret;
    }
};

class Solution2 {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t ret = 0;
        uint32_t power = 31;
        int mask = 1;
        
        while (n>0){
            ret += (n&mask) << power;
            power -= 1;
            n >>= 1;
        }
        return ret;
    }
};
