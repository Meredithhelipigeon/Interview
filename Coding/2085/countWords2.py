class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        wordToOccurance = {}
        for word in words1:
            if word in wordToOccurance:
                wordToOccurance[word]+=1
            else:
                wordToOccurance[word]=1

        for word in words2:
            if word in wordToOccurance:
                if wordToOccurance[word]==1:
                    wordToOccurance[word] -= 1
                elif wordToOccurance[word]==0:
                    wordToOccurance[word] = -1
        
        ret = 0
        for word in wordToOccurance:
            if wordToOccurance[word]==0:
                ret += 1
        return ret
