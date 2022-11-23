class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""

        ret = strs[0]
        for i in range(1,len(strs)):
            for j in range(min(len(ret), len(strs[i]))):
                if ret[j]!=strs[i][j]:
                    ret = ret[:j]
                    break
            if len(ret)>len(strs[i]):
                ret = ret[:len(strs[i])]
        return ret
