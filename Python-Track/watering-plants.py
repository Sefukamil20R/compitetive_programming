class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
            
            step=0
            orig=capacity
            for i in range(len(plants)):
                if capacity >=plants[i]:
                    step+=1
                    capacity-=plants[i]
                else:
                    step+=2*i+1
                    capacity=orig-plants[i]
               
            return step
                    
                
        