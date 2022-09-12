class Solution:
    # Time efficiency: O(nlogn)
    def maxSlidingWindow_Sol1(self, nums: List[int], k: int) -> List[int]:
        h = []
        
        for i in range(k-1):
            heapq.heappush(h, (-nums[i],i))
        ret = []
        
        for i in range(k-1, len(nums)):
            heapq.heappush(h, (-nums[i],i))
            value, valuePos = heapq.heappop(h)
            while valuePos <= i-k:
                value, valuePos = heapq.heappop(h)
            heapq.heappush(h, (value,valuePos))
            ret.append(-value)
        
        return ret
    
    # Time efficiency: O(n*k)
    def maxSlidingWindow_Sol2(self, nums: List[int], k: int) -> List[int]:
        if k==1: return nums
        maximumCandidate = []
        
        for i in range(k-1):
            if len(maximumCandidate)==0:
                maximumCandidate.append(nums[i])
            else:
                while len(maximumCandidate)>0 and maximumCandidate[-1] < nums[i]:
                    maximumCandidate.pop()
                maximumCandidate.append(nums[i])
        ret = []

        for i in range(k-1, len(nums)):
            if len(maximumCandidate)==0:
                maximumCandidate.append(nums[i])
            else:
                while len(maximumCandidate)>0 and maximumCandidate[-1] < nums[i]:
                    maximumCandidate.pop()
                maximumCandidate.append(nums[i])
            if i-k>=0 and maximumCandidate[0]==nums[i-k]:
                maximumCandidate.pop(0)
            ret.append(maximumCandidate[0])
        
        return ret

    # Time efficiency: O(n)
    # use deque; the method is similar to the second one but since dequeue supports popleft and popright
    # so that it could make sure that add to left and add to right operations are both in O(1)
    def maxSlidingWindow_Sol3(self, nums: List[int], k: int) -> List[int]:
        if k==1: 
            return nums
        elif k==0 or len(nums)==0:
            return []
        maximumCandidate = deque()
        
        def clean_dequeue(cur):
            while len(maximumCandidate)>0 and maximumCandidate[-1] < nums[i]:
                    maximumCandidate.pop()
            
        for i in range(k-1):
            clean_dequeue(nums[i])
            maximumCandidate.append(nums[i])
        ret = []

        for i in range(k-1, len(nums)):
            clean_dequeue(nums[i])
            maximumCandidate.append(nums[i])
            if i-k>=0 and maximumCandidate[0]==nums[i-k]:
                maximumCandidate.popleft()
            ret.append(maximumCandidate[0])
        
        return ret

