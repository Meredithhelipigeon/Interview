class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ret = 0
        start = end = 0
        curFrequencies = {}
        curPair = 0
        
        while end < len(nums):
            curNum = nums[end]
            if curNum in curFrequencies:
                curPair +=  curFrequencies[curNum]
                curFrequencies[curNum] += 1
            else:
                curFrequencies[curNum] = 1
            while curPair>=k:
                curPair -= curFrequencies[nums[start]]-1
                curFrequencies[nums[start]] -= 1
                start += 1
            ret += end-start+1
            end += 1
            
        return len(nums)*(len(nums)+1)//2 - ret
            
