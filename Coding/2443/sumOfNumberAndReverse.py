class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        cur = []
        reversedCur = []
        
        def checkIfFind(curNum):
            if curNum < 0: return False
            if curNum == 0:
                for i in range(len(cur)):
                    if cur[i]!=reversedCur[len(cur)-1-i]:
                        return False
                return True
            n = curNum % 10
            for i in range(10):
                cur.append(i)
                reversedCur.append((n-i)%10)
                if n-i < 0:
                    if checkIfFind(curNum //10 - 1): 
                        return True
                else: 
                    if checkIfFind(curNum //10): 
                        return True
                cur.pop()
                reversedCur.pop()
            return False
        return checkIfFind(num)
