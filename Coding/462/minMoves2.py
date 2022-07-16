class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        ret=0
        nums=sorted(nums)
        for i in range(len(nums)//2):
            ret+=nums[len(nums)-i-1]-nums[i]
        return ret
