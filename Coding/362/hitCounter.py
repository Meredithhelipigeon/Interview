import collections
class HitCounter:
    def __init__(self):
        self.h = collections.deque([])
        self.hits = 0
    
    def cleanUp(self, timestamp):
        while (len(self.h)>0 and timestamp-self.h[0][0]>=300):
            self.hits -= self.h[0][1]
            self.h.popleft()

    def hit(self, timestamp: int) -> None:
        if len(self.h)>0 and self.h[-1][0]==timestamp:
            self.h[-1][1]+=1
        else:
            self.h.append([timestamp,1])
        self.hits += 1
        self.cleanUp(timestamp)

    def getHits(self, timestamp: int) -> int:
        self.cleanUp(timestamp)
        return self.hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
