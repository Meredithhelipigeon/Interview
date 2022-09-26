class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1_to_count = {}
        words2_to_count = {}
        
        for w in words1:
            if w in words1_to_count:
                words1_to_count[w] += 1
            else:
                words1_to_count[w] = 1
        
        for w in words2:
            if w in words2_to_count:
                words2_to_count[w] += 1
            else:
                words2_to_count[w] = 1
        ret = 0
        for w in words1_to_count:
            if words1_to_count[w]==1 and words2_to_count.get(w)==1:
                ret += 1
    
        return ret
