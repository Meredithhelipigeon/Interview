class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        nums = []
        curIntSum = 0
        
        while n > 0:
            nums.append(n%10)
            curIntSum += n%10
            n //= 10
        
        ret = 0
        index = 0

        while curIntSum > target:
            ret += (10 - nums[index]) * (10**index)
            curIntSum -= nums[index]
            nums[index] = 0
            
            while index+1 < len(nums):
                nums[index+1] += 1
                if nums[index+1] == 10:
                    nums[index+1] = 0
                    curIntSum -= 9
                else:
                    curIntSum += 1
                    index += 1
                    break
                index += 1

        return ret
