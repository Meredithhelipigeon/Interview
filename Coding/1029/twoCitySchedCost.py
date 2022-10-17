class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        aNum = 0
        bNum = 0
        costs = sorted(costs, key=lambda x: -abs(x[0]-x[1]))
        n = len(costs)//2
        ret = 0
        
        for c in costs:
            if aNum < n and bNum < n:
                if c[0]<c[1]:
                    aNum += 1
                    ret += c[0]
                else:
                    ret += c[1]
                    bNum += 1
            elif aNum < n:
                aNum += 1
                ret += c[0]
            else:
                ret += c[1]
                bNum += 1
                
        return ret
