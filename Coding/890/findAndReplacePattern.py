class Solution(object):
    # Time efficiency: O(len(words)*len(pattern)), Space efficiency: O(len(pattern)*len(words))
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def ifPattern(word):
            word_to_pattern = {}
            pattern_to_word = {}
            for i in range(len(word)):
                if word[i] not in word_to_pattern and pattern[i] not in pattern_to_word:
                    word_to_pattern[word[i]] = pattern[i]
                    pattern_to_word[pattern[i]] = word[i]
                elif word[i] not in word_to_pattern or pattern[i] not in pattern_to_word:
                    return False
                else:
                    if word_to_pattern[word[i]] != pattern[i] or pattern_to_word[pattern[i]] != word[i]:
                        return False
            return True
        
        ret = []
        for word in words:
            if ifPattern(word):
                ret.append(word)
        return ret
