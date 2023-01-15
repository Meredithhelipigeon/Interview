class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1]-nums[0]
        for i in range(len(nums)-1):
            ma = max(nums[-1]-k,nums[i]+k)
            mi = min(nums[0]+k, nums[i+1]-k)
            ans = min(ma-mi, ans)
        return ans
