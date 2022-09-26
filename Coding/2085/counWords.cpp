class Solution {
public:
    int countWords(vector<string>& words1, vector<string>& words2) {
        std::unordered_map<string,int> word_to_count;
        
        for(auto w: words1){
            if (word_to_count.find(w)!=word_to_count.end()){
                word_to_count[w] += 1;
            } else {
                word_to_count[w] = 1;
            }
        }
        
        for(auto w: words2){
            if (word_to_count.find(w)!=word_to_count.end() && word_to_count[w]==1){
                word_to_count[w] = -1;
            } else if (word_to_count.find(w)!=word_to_count.end() && word_to_count[w]==-1) {
                word_to_count[w] = 0;
            }
        }
        
        int ret = 0;
        for(auto w: word_to_count){
            if (w.second==-1){
                ret += 1;
            }
        }
        return ret;
    }
};
