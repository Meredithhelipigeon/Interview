class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        nums_costs = zip(nums, cost)
        nums_costs = sorted(nums_costs)
        prefix = []
        cur = 0
        
        for nc in nums_costs:
            prefix.append(cur)
            cur += nc[1]
        
        ret = 0
        for nc in nums_costs:
            ret += abs(nc[0]-nums_costs[0][0])*nc[1]
        
        for i in range(1, len(cost)):
            diff = (nums_costs[i][0]-nums_costs[i-1][0])
            curRet = ret - diff*(cur - prefix[i]) + diff * prefix[i]
            ret = min(ret, curRet)
               
        return ret
