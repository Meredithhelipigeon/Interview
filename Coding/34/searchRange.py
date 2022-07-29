class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret=[-1,-1]
        start = bisect_left(nums,target)
        end = bisect_right(nums,target)-1
        
        if 0<=start<len(nums) and nums[start]==target:
            ret[0]=start
        if 0<=end<len(nums) and nums[end]==target:
            ret[1]=end
        return ret
