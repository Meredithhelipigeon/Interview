class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ifHasLeftSmaller = [False]*len(nums)
        ifHasRightBigger = [False]*len(nums)
        
        curMin = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>curMin:
                ifHasLeftSmaller[i]=True
            else:
                curMin = nums[i]
        
        curMax = nums[-1]
        for i in range(len(nums)-1, -1,-1):
            if nums[i]<curMax:
                ifHasRightBigger[i]=True
            else:
                curMax = nums[i]
        
        for i in range(len(nums)):
            if ifHasLeftSmaller[i] and ifHasRightBigger[i]:
                return True
        return False
