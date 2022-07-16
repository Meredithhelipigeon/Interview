class Solution:
    def maximumSwap1(self, num: int) -> int:
        nums = [int(x) for x in str(num)]
        curMax = nums[-1]
        curMaxIndex=len(nums)-1
        temp = [-1]*len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            if curMax > nums[i]:
                temp[i] = curMaxIndex
            elif curMax < nums[i]:
                curMax = nums[i]
                curMaxIndex = i
        
        for i in range(len(nums)-1):
            if temp[i]!=-1:
                nums[i],nums[temp[i]]=nums[temp[i]],nums[i]
                strings = [str(integer) for integer in nums]
                a_string = "". join(strings)
                return int(a_string)
        return num
