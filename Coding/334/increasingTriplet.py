class Solution:
    # Time efficiency: O(n)
    # Space complexity: O(n)
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
    
    # Time efficiency: O(n)
    # Space complexity: O(1)
    def increasingTriplet2(self, nums: List[int]) -> bool:
        smallest = second_smallest = float('inf')
        
        for i in range(len(nums)):
            if nums[i] < smallest:
                smallest = nums[i]
            elif smallest < nums[i] < second_smallest:
                second_smallest = nums[i]
            elif nums[i]>second_smallest:
                return True
        return False
