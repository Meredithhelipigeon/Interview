class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ret = [0]*length
        for startIndex, endIndex, inc in updates:
            ret[startIndex]+=inc
            if endIndex+1<length:
                ret[endIndex+1]-=inc
        
        for i in range(1, length):
            ret[i]+=ret[i-1]
        return ret
