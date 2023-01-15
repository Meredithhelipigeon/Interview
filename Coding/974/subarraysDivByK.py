class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ret = 0
        curSum = 0
        prefixToFreq = [0]*k
        prefixToFreq[0] += 1
        
        for num in nums:
            curSum += num
            ret += prefixToFreq[(curSum-k)%k]
            prefixToFreq[curSum%k]+=1
        return ret
