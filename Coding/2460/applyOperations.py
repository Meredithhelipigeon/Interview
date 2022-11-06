class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return []
        
        for i in range(1, len(nums)):
            if nums[i-1]==nums[i]:
                nums[i-1]*=2
                nums[i]=0
        
        ret = []
        zeroNum = 0
        
        for n in nums:
            if n!=0:
                ret.append(n)
            else:
                zeroNum += 1
        ret.extend([0]*zeroNum)
                
        return ret
                
