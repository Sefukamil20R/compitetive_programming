class Solution:
     def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        a=min(start,destination)
        b=max(start,destination)
        return min(sum(distance[a:b]),sum(distance)-sum(distance[a:b]))
    
    #     clocks=0
    #     while i != destination:
    #         clocks += distance[i]
    #         i = (i + 1) % len(distance)
    #     antis = 0
    #     i = start
    #     while i != destination:
    #         i = (i - 1) % len(distance)
    #         antis += distance[i]
    #     return min(clocks, antis)
        
        
       
   
        
            