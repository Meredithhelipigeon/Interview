class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums)<k:
            return 0     
        
        # initialization
        curElements = {}
        curSum = 0
        for i in range(k-1):
            if nums[i] in curElements:
                curElements[nums[i]] += 1
            else:
                curElements[nums[i]] = 1
            curSum += nums[i]
        ret = 0
        
        for i in range(k-1, len(nums)):
            if nums[i] in curElements:
                curElements[nums[i]] += 1
            else:
                curElements[nums[i]] = 1
            curSum += nums[i]
            if i-k>=0:
                curElements[nums[i-k]] -= 1
                if curElements[nums[i-k]]==0:
                    del curElements[nums[i-k]]
                curSum -= nums[i-k]
            if len(curElements)==k:
                ret = max(ret, curSum)
        return ret
        
