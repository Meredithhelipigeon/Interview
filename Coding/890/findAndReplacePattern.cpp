class Solution {
public:
    // Time efficiency: O(len(pattern)*len(words)); Space Complexity: O(len(pattern)*len(words))
    // The characters are not important, the important thing is the order. 
    // Therefore, it is easy to turn the characters to numbers and the compare. 
    vector<int> find_pattern(string word) {
        int cur = 0;
        map<char, int> chr_to_int;
        vector<int> ret;
        for(auto c: word){
            if (chr_to_int.find(c) == chr_to_int.end()) {
                chr_to_int[c]=cur;
                cur+=1;
            }
            ret.emplace_back(chr_to_int[c]);
        }
        return ret;
    }
    
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        vector<int> intPattern = find_pattern(pattern);
        vector<string> ret;
        for(auto word: words){
            vector<int> intCurPattern = find_pattern(word);
            if (intCurPattern == intPattern) {
                ret.emplace_back(word);
            }
        }
        return ret;
    }
};
