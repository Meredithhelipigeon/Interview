class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter=sum(matchsticks)
        if perimeter%4 != 0: return False
        squareLen=perimeter//4
        
        curLen=[squareLen,squareLen,squareLen,squareLen]
        
        def build(index: int) -> bool:
            if index==len(matchsticks):
                return True
            for i in range(4):
                if curLen[i]>=matchsticks[index]:
                    curLen[i]-=matchsticks[index]
                    if build(index+1): 
                        return True
                    curLen[i]+=matchsticks[index]
            return False
        
        return build(0)
