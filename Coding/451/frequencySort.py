class Solution:
    def frequencySort(self, s: str) -> str:
        ret = []
        charToCount = {}
        
        for c in s:
            if c in charToCount:
                charToCount[c]+=1
            else:
                charToCount[c]=1
        sortedChars = sorted(charToCount.keys(), key=lambda char: -charToCount[char])
        for c in sortedChars:
            ret.append(charToCount[c]*c)
            
        return "".join(ret)
