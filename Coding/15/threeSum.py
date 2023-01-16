class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(curIndex):
            su = -nums[curIndex]
            ret = []
            visitedNums = set()
            addedNums = set()
            
            for i in range(curIndex+1,len(nums)):
                if su-nums[i] in visitedNums:
                    if not(nums[i] in addedNums or su-nums[i] in addedNums):
                        ret.append([-su, su-nums[i], nums[i]])
                    addedNums.add(nums[i])
                visitedNums.add(nums[i])
            return ret
        
        ret = []
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i-1]!=nums[i]:
                ret.extend(twoSum(i))
        return ret
