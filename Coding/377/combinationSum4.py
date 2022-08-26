class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        global curSum
        curSum = 0
        global ret 
        ret = 0
        nums = sorted(nums)
        def dfs():
            global curSum
            global ret
            if curSum == target:
                ret+=1
            for can in nums:
                if can+curSum > target:
                    break
                elif can+curSum <= target:
                    curSum+=can
                    dfs()
                    curSum-=can
            return
        dfs()
        return ret
