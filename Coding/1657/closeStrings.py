class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def checkCharToCount(w):
            charToNum = {}
            for c in w:
                if c in charToNum:
                    charToNum[c]+=1
                else:
                    charToNum[c]=1
            return charToNum
        
        charToNumWord1 = checkCharToCount(word1)
        charToNumWord2 = checkCharToCount(word2)

        # check if the characters are the same
        if set(charToNumWord1.keys())!=set(charToNumWord2.keys()):
            return False
        
        # get the comination of countNumbers
        numTocCount = {}
        for c in charToNumWord1:
            num = charToNumWord1[c]
            if num in numTocCount:
                numTocCount[num]+=1
            else:
                numTocCount[num]=1
        
        for c in charToNumWord2:
            num = charToNumWord2[c]
            if num in numTocCount:
                numTocCount[num]-=1
                if numTocCount[num]==0:
                    del numTocCount[num]
            else:
                return False
        
        return len(numTocCount)==0
