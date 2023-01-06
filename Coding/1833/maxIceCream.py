class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        ret = 0
        for cost in costs:
            if coins >= cost:
                coins -= cost
                ret += 1
            else:
                return ret
        return ret
