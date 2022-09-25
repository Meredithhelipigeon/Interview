class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ret = []
        
        def backTrack(path, cur, adds_on, minus_on, curIndex):
            if curIndex==len(num):
                cur = cur + adds_on - minus_on
                if cur==target: 
                    ret.append("".join(path))
                    return True
                else: 
                    return False
            retFalue = False
            last = len(num)
            if num[curIndex] == "0": last = curIndex + 1
            if curIndex==0:
                for i in range(curIndex, last):
                    curNum = int(num[curIndex:i+1])
                    path = [str(curNum)]
                    if backTrack(path, cur, curNum, minus_on, 1+i):
                        retFalue = True
            else:
                for i in range(curIndex, last):
                    curNum = int(num[curIndex:i+1])
                    old_adds_on = adds_on
                    old_minus_on = minus_on
                    
                    # minus
                    path += "-"
                    path.append(str(curNum))
                    cur = cur + adds_on - minus_on
                    adds_on = 0
                    minus_on = curNum
                    if (backTrack(path, cur, adds_on, minus_on, 1+i)):
                        retFalue = True
                    for j in range(2):
                        path.pop()
                    cur -= old_adds_on - old_minus_on
                    adds_on = old_adds_on
                    minus_on = old_minus_on

                    # add 
                    path += "+" 
                    path.append(str(curNum))
                    cur = cur + adds_on - minus_on
                    minus_on = 0
                    adds_on = curNum
                    if (backTrack(path, cur, adds_on, minus_on, 1+i)):
                        retFalue = True
                    for j in range(2):
                        path.pop()
                    cur -= old_adds_on - old_minus_on
                    adds_on = old_adds_on
                    minus_on = old_minus_on
                    
                    # times
                    if adds_on != 0: adds_on *= curNum
                    else: minus_on *= curNum
                    path += "*" 
                    path.append(str(curNum))
                    if (backTrack(path, cur, adds_on, minus_on, 1+i)):
                        retFalue = True
                    for j in range(2):
                        path.pop()
                    adds_on = old_adds_on
                    minus_on = old_minus_on
            return retFalue
        
        backTrack([],0,0,0,0)
        return ret
