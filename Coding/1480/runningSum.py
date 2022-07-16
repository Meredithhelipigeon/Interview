class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur = 0
        ret = []
        
        for n in nums:
            cur+=n
            ret.append(cur)
        
        return ret
