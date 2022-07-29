class Solution(object):
    # Insertion-Sort
    # Time Complexity: O(n^2), Space Comlexity: O(n)
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            cur = i
            while cur+1 < len(nums) and nums[cur]>nums[cur+1]:
                nums[cur],nums[cur+1]=nums[cur+1],nums[cur]
                cur+=1
            ret[i]=cur-i
        return ret
