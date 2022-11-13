class Solution:
    def reverseWords(self, s: str) -> str:
        curWord = []
        ret = []
        
        for ss in s:
            if ss != " ":
                curWord.append(ss)
            else:
                if len(curWord)>0:
                    ret.append("".join(curWord))
                    curWord = []
        if len(curWord)>0:
            ret.append("".join(curWord))
        ret = reversed(ret)
        
        return " ".join(ret)
