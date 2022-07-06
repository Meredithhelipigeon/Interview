class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        
        second_last=0
        last=1
        cur=1
        
        for i in range(2,n+1):
            cur=second_last+last
            second_last=last
            last=cur
        
        return cur
