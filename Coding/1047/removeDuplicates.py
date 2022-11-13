class Solution:
    def removeDuplicates(self, s: str) -> str:
        charToCount = {}
        ret = []

        for c in s:
            if len(ret)>0 and ret[-1]==c:
                ret.pop()
            else:
                ret.append(c)
        
        return "".join(ret)
