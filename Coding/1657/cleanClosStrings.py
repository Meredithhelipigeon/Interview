class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def getWordMap(w):
            charToNum = {}
            for c in w:
                if c in charToNum:
                    charToNum[c]+=1
                else:
                    charToNum[c]=1
            return charToNum
        def getFrequencyList(wordMap):
            ret = []
            for (w,count) in wordMap.items():
                ret.append(count)
            return ret
        
        charToCountWord1 = getWordMap(word1)
        charToCountWord2 = getWordMap(word2)

        # Condition1: check if the characters are the same
        if set(charToCountWord1.keys())!=set(charToCountWord2.keys()):
            return False
        
        # Condition2: check the frequency
        word1FrequencyList =  sorted(getFrequencyList(charToCountWord1))
        word2FrequencyList =  sorted(getFrequencyList(charToCountWord2))
        
