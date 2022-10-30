class Solution:
    def averageValue(self, nums: List[int]) -> int:
        retSum = 0
        retNum = 0
        for n in nums:
            if n % 6 == 0:
                retSum += n
                retNum += 1
        if retNum == 0:
            return 0
        return retSum // retNum
