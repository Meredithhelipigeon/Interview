class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        dpExpress = [expressCost]+[0]*(len(express))
        dpRegular = [0]*(len(regular)+1)
        costs = []
        
        for i in range(1,len(regular)+1):
            dpExpress[i] = min(dpExpress[i-1]+express[i-1], dpRegular[i-1]+regular[i-1]+expressCost)
            dpRegular[i] = min(dpRegular[i-1]+regular[i-1],dpExpress[i-1]+express[i-1])
            costs.append(min(dpExpress[i],dpRegular[i]))
        return costs
