class TimeMap:

    def __init__(self):
        # (key:key, value: a list of tuple(timestamp, value))
        self.keys_to_valueList = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keys_to_valueList:
            self.keys_to_valueList[key].append((timestamp, value))
        else:
            self.keys_to_valueList[key] = [(timestamp, value)]
                
    def get(self, key: str, timestamp: int) -> str:
        if key in self.keys_to_valueList:
            valueList = self.keys_to_valueList[key]
            if valueList[-1][0]<=timestamp:
                return valueList[-1][1]
            i = bisect.bisect_left(self.keys_to_valueList[key], (timestamp, ""))
            if valueList[i][0] == timestamp:
                return valueList[i][1]
            else:
                if i-1 >= 0:
                    return valueList[i-1][1]
                else:
                    return ""
        else:
            return ""
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
