class NumArray:
    # Space effciency: O(n)
    # Time efficiency: O(n)
    def __init__(self, nums: List[int]):
        self.sumNum = []
        cur = 0
        for nn in nums:
            cur += nn
            self.sumNum.append(cur)
        self.nums = nums
        self.ownCache = [float('inf')]*len(nums)
        self.minCache = len(nums)

    # Time efficiency: O(1)
    def update(self, index: int, val: int) -> None:
        self.ownCache[index] = val-self.nums[index]
        self.minCache = min(index,self.minCache)  

    # Time efficiency: O(n)
    def sumRange(self, left: int, right: int) -> int:
        if self.minCache <= right:
            cur = 0
            for i in range(self.minCache,len(self.nums)):
                if self.ownCache[i] != float('inf'):
                    cur += self.ownCache[i]
                    self.nums[i] += self.ownCache[i]
                    self.ownCache[i] = float('inf')
                self.sumNum[i]+=cur
            self.minCache = len(self.nums)
            
        if left==0:
            return self.sumNum[right]
        return self.sumNum[right]-self.sumNum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# Sqrt Decomposition
# Sqrt Decomposition is a method (or a data structure) that allows you to perform some common operations 
# (finding sum of the elements of the sub-array, finding the minimal/maximal element, etc.) in O(sqrt(n)) operations, 
#  which is much faster than O(n) for the trivial algorithm.
class NumArray2:
    # Space effciency: O(n)
    def __init__(self, nums: List[int]):
        self.blocks = []
        self.blockLen = int(sqrt(len(nums)))
        cur = 0
        for i in range(len(nums)):
            if i % self.blockLen == 0:
                self.blocks.append(cur)
                cur = 0
            cur += nums[i]
        self.nums = copy.deepcopy(nums)
        
    def update(self, index: int, val: int) -> None:
        if index//self.blockLen+1 < len(self.blocks):
            self.blocks[index//self.blockLen+1] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        ret = 0
        startBlock = left // self.blockLen
        endBlock = right // self.blockLen
        
        if startBlock < endBlock:
            ret += sum(self.blocks[startBlock+1:endBlock+1])
            for i in range(startBlock*self.blockLen,left):
                ret -= self.nums[i]
            for i in range(endBlock*self.blockLen,right+1):
                ret += self.nums[i]
        else:
            ret = sum(self.nums[left:right+1])
        return ret
