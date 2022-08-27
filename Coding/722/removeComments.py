class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ret = []
        inline_comments = False
        curLine = []
        for s in source:
            i = 0
            while i < len(s):
                if inline_comments:
                    if i!= len(s)-1 and s[i:i+2] == "*/":
                        inline_comments = False
                        i += 2
                        continue
                else:   
                    if i!= len(s)-1:
                        if s[i:i+2] == "//":
                            break
                        elif s[i:i+2] == "/*":
                            inline_comments = True
                            i+=2
                            continue
                    curLine.append(s[i])
                i += 1
            if len(curLine)>0 and not inline_comments:
                curLine = ''.join(curLine)
                ret.append(curLine)
                curLine = []
        return ret
