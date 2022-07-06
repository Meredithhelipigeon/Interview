class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        edges = {}
        for n in nums:
            if n-1 in edges:
                edges[n-1] = n
            if n+1 in edges:
                edges[n]=n+1
            else:
                edges[n]=False
        
        ret = 0
        for n in edges:
            if edges[n]==False:
                cur=1
                while n-cur in edges:
                    cur+=1
                ret=max(cur,ret)
        return ret
