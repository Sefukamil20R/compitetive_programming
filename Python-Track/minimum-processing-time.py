class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
             tasks.sort()
             processorTime.sort( reverse= True )
             i = 0
             maxx = 0
             for j in range (len(tasks)):
                 maxx = max (processorTime[i] + tasks[j], maxx)
                 if ((j+1)%4 == 0):
                       i += 1
             return maxx 
            
                    


            
            
                 

        