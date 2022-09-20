class Solution {
public:
    int getSum(int a, int b) {
        int signedOp =1;
        int temp = 0;
        if (a*b > 0) {
            if (a<0) {
                signedOp = -1;
                a *= -1;
                b *= -1;
            }
            
            while (b > 0) {
                int oldA = a;
                int oldB = b;
                a = oldA ^ oldB;
                b = (oldA & oldB) << 1;
            }
        } else {
            if (max(a,b) < abs(min(a,b))){
                signedOp = -1;
            }
            a = max(a, (-1)*a);
            b = max(b, (-1)*b);
            temp = 0;
            // Always make sure that a is bigger
            if (a<b){
                temp = a;
                a = b;
                b = temp;
            }
            while (b > 0){
                int oldA = a;
                int oldB = b;
                a = oldA ^ oldB;
                b = ((~oldA) & oldB) << 1;
            }
        }
        return a*signedOp;
    }
};
