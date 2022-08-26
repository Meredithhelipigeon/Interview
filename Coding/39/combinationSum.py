class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cur = []
        global curSum
        curSum = 0
        ret = []
        global last 
        last = 0
        def dfs():
            global curSum, last
            if curSum == target:
                ret.append(copy.deepcopy(cur))
            for i in range(last,len(candidates)):
                can = candidates[i]
                if can+curSum > target:
                    break
                elif can+curSum <= target:
                    cur.append(can)
                    curSum+=can
                    last = i
                    dfs()
                    cur.pop()
                    curSum-=can
            return
        dfs()
        return ret
