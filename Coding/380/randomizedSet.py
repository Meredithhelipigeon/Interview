class RandomizedSet:

    def __init__(self):
        self.nums_to_positions = {}
        self.currentList = []
        
    def insert(self, val: int) -> bool:
        if val in self.nums_to_positions:
            return False
        else:
            self.nums_to_positions[val]=len(self.currentList)
            self.currentList.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.nums_to_positions:
            rmPosition = self.nums_to_positions[val]
            self.nums_to_positions[self.currentList[-1]] = rmPosition
            self.currentList[rmPosition] = self.currentList[-1]
            self.currentList.pop()
            del self.nums_to_positions[val]
            return True
        else: return False
        
    def getRandom(self) -> int:
        randomInt = random.randint(0, len(self.currentList)-1)
        return self.currentList[randomInt]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
