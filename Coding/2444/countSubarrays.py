class Solution:
    def countSubarrays1(self, nums: List[int], minK: int, maxK: int) -> int:
        def checkNum(segment):
            ret = 0
            for i in range(len(segment)):
                curMin = segment[i]
                curMax = segment[i]
                for j in range(i, len(segment)):
                    curMin = min(segment[j], curMin)
                    curMax = max(segment[j], curMax)
                    if curMin==minK and curMax==maxK: ret += 1
            return ret
        
        stops = []
        for i in range(len(nums)):
            if not (minK<=nums[i]<=maxK):
                stops.append(i)
        stops.append(len(nums))
        
        ret = 0
        last = 0
        for s in stops:
            segment = nums[last:s]
            ret += checkNum(segment)
            last = s
        return ret
    
    # Sliding window version
    def countSubarrays2(self, nums: List[int], minK: int, maxK: int) -> int:
        def checkNum(segment):
            invalidNum = left = 0
            minKNum = maxKNum = 0
            for i in range(len(segment)):
                elem = segment[i]
                if elem == minK: minKNum += 1
                if elem == maxK: maxKNum += 1
                while minKNum >= 1 and maxKNum >= 1:
                    if segment[left] == minK: minKNum -= 1
                    if segment[left] == maxK: maxKNum -= 1
                    left += 1
                invalidNum += i - left + 1
            combNum = len(segment) * (len(segment) - 1) // 2 + len(segment)
            return combNum - invalidNum
        
        stops = []
        for i in range(len(nums)):
            if not (minK<=nums[i]<=maxK):
                stops.append(i)
        stops.append(len(nums))
        
        ret = 0
        last = -1
        for s in stops:
            segment = nums[last+1:s]
            ret += checkNum(segment)
            last = s
        return ret

    def countSubarrays3(self, nums: List[int], minK: int, maxK: int) -> int:
        def checkNum(segment):
            mostRecentMinK = mostRecentMaxK = -1
            ret = 0
            for i in range(len(segment)):
                if segment[i]==minK: mostRecentMinK = i
                if segment[i]==maxK: mostRecentMaxK = i
                ret += (i+1) - (i - min(mostRecentMinK, mostRecentMaxK))
            return ret    
        
        stops = []
        for i in range(len(nums)):
            if not (minK<=nums[i]<=maxK):
                stops.append(i)
        stops.append(len(nums))
        
        ret = 0
        last = -1
        for s in stops:
            segment = nums[last+1:s]
            ret += checkNum(segment)
            last = s
        return ret

    def countSubarrays3(self, nums: List[int], minK: int, maxK: int) -> int:
        def checkNum(segment):
            mostRecentMinK = mostRecentMaxK = -1
            ret = 0
            for i in range(len(segment)):
                if segment[i]==minK: mostRecentMinK = i
                if segment[i]==maxK: mostRecentMaxK = i
                ret += (i+1) - (i - min(mostRecentMinK, mostRecentMaxK))
            return ret    
        
        stops = []
        for i in range(len(nums)):
            if not (minK<=nums[i]<=maxK):
                stops.append(i)
        stops.append(len(nums))
        
        ret = 0
        last = -1
        for s in stops:
            segment = nums[last+1:s]
            ret += checkNum(segment)
            last = s
        return ret

    def countSubarrays4(self, nums: List[int], minK: int, maxK: int) -> int:
        start = 0
        mostRecentMinK = mostRecentMaxK = -1
        ret = 0
        
        for i in range(len(nums)):
            if nums[i]<minK or nums[i]>maxK:
                start=i+1
            else:
                if nums[i]==minK: mostRecentMinK=i
                if nums[i]==maxK: mostRecentMaxK=i
                ret += (i-start+1)- (i-max(min(mostRecentMinK,mostRecentMaxK), start-1))
        return ret
