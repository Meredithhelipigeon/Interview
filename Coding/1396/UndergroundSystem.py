class UndergroundSystem:

    def __init__(self):
        # "start end": [num, total]
        self.time_tracker = {}
        # id: [startStation, t]
        self.current_passenger = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.current_passenger[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        timeDiff = t - self.current_passenger[id][1]
        start_and_end_stations = self.current_passenger[id][0] + " " + stationName
        if start_and_end_stations in self.time_tracker:
            self.time_tracker[start_and_end_stations][0] += 1
            self.time_tracker[start_and_end_stations][1] += timeDiff
        else:
            self.time_tracker[start_and_end_stations] = [1, timeDiff]
        del self.current_passenger[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        start_and_end_stations = startStation + " " + endStation
        return self.time_tracker[start_and_end_stations][1] / (self.time_tracker[start_and_end_stations][0]*1.0)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
