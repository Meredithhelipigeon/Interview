class Solution:
    def firstUniqChar1(self, s: str) -> int:
        char_to_frequencies_position = OrderedDict()
        
        for i in range(len(s)):
            char = s[i]
            if char in char_to_frequencies_position:
                char_to_frequencies_position[char][0] += 1
            else:
                char_to_frequencies_position[char] = [1,i]
    
        for key in char_to_frequencies_position:
            if char_to_frequencies_position[key][0] == 1:
                return char_to_frequencies_position[key][1]
        return -1

    def firstUniqChar2(self, s: str) -> int:
        char_to_frequencies = {}
        
        for char in s:
            if char in char_to_frequencies:
                char_to_frequencies[char] += 1
            else:
                char_to_frequencies[char] = 1
                
        for i in range(len(s)):
            if char_to_frequencies[s[i]] == 1:
                return i
        
        return -1
    
    def firstUniqChar3(self, s: str) -> int:
        counter = collections.Counter(s)
                
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        
        return -1
