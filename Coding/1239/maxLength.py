class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.ret = 0
        self.curMap = [False] * 26
        self.wordLength = 0
        
        def makeWord(cur):
            if cur==len(arr):
                self.ret = max(self.ret, self.wordLength)
                return
            
            ifUnique = True
            word = arr[cur]
            tempMap = copy.deepcopy(self.curMap)
            for i in range(len(word)):
                c = word[i]
                if self.curMap[ord(c)-ord('a')]:
                    ifUnique = False
                self.wordLength += 1
                self.curMap[ord(c)-ord('a')]=True
            
            if ifUnique:
                makeWord(cur+1)
            self.curMap = tempMap
            self.wordLength -= len(word)
            
            makeWord(cur+1)
        
        makeWord(0)
        return self.ret
