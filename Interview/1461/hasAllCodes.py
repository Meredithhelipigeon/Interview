class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        num_set = set()
        
        # Step 1. Check the first one
        initial=[]
        cur=-1
        for i in range(min(k,len(s))):
            initial.append(s[i])
        cur=int(''.join(initial),2)
        num_set.add(cur)
        
        max_in_k = 2**(k-1)
        total = 2**k
        
        # Step 2. Add the second one
        for j in range(k,len(s)):
            if s[j-k]=='1':
                cur-=max_in_k
            cur*=2
            if s[j]=='1':
                cur+=1
            num_set.add(cur)
            if len(num_set)==total:
                return True
            
        return False
