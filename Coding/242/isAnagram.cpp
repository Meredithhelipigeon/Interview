class Solution {
public:
    bool isAnagram(string s, string t) {
        int lettersMap[26] = {};
        const char base = 'a';
        
        if (s.size()!=t.size()) return false;
        
        for(int i = 0; i < t.size(); i++){
            lettersMap[t[i]-base] += 1;
            lettersMap[s[i]-base] -= 1;
        }
        
        for(int i = 0; i < 26; i++){
            if (lettersMap[i] != 0) return false;
        }
        return true;
    }
};
