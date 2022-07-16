class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        new_words = [w[::-1] for w in words]
        global ret
        ret=0
        
        def bucket_sort(wds,cur):
            global ret
            if len(wds)==1:
                ret+=len(wds[0])+1
                return
            words_lists = [[] for i in range(26)]
            
            for wd in wds:
                if len(wd)>cur:
                    words_lists[ord(wd[cur])-ord('a')].append(wd)
                    
            all_last = True
            for i in range(26):
                if len(words_lists[i])>0:
                    bucket_sort(words_lists[i],cur+1)
                    all_last=False
            if all_last:
                ret+=len(wds[0])+1
        
        bucket_sort(new_words,0)
        return ret
