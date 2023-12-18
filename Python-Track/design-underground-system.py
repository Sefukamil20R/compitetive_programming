class UndergroundSystem:

    def __init__(self):
        self.hashmap = {}
        self.collective = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.hashmap[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.collective[(self.hashmap[id][0], stationName)].append(t - self.hashmap[id][1]) 
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:       
        return float(sum(self.collective[(startStation, endStation)])) / len(self.collective[(startStation, endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)  