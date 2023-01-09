class Solution:
    def calculate(self, s: str) -> int:
        def calcualteDivideTimesStack():
            base = int("".join(reversed(curNum)))
            while len(divideTimesStack)>0:
                curItem = divideTimesStack.pop()
                if curItem == "*":
                    base *= divideTimesStack.pop()
                else:
                    base //= divideTimesStack.pop()
            return base
        
        # Step 1. cleanup the empty space
        s = ["+"] + [ss for ss in s if ss != " "]
        curNum = []
        ret = 0
        divideTimesStack = []
        
        # Step 2. calculate the expression by different cases
        for i in range(len(s)-1, -1, -1):
            if "0"<=s[i]<="9":
                curNum.append(s[i])
            else:
                if s[i]=="*" or s[i]=="/":
                    divideTimesStack.append(int("".join(reversed(curNum))))
                    divideTimesStack.append(s[i])
                else:
                    if s[i]=="+":
                        ret += calcualteDivideTimesStack()
                    else:
                        ret -= calcualteDivideTimesStack()
                curNum = []
        return ret
