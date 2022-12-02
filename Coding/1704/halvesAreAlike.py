class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel_chars = set(["a","e","i","o","u", "A", "E", "I", "O", "U"])
        def checkVowel(c):
            if c in vowel_chars:
                return True
            else:
                return False
        
        vowelNum = 0
        for i in range(len(s)):
            if i < len(s)/2:
                if checkVowel(s[i]):
                    vowelNum += 1
            else:
                if checkVowel(s[i]):
                    vowelNum -= 1
                    
        return vowelNum==0
