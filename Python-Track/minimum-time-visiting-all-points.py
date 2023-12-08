class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        summ=0
        for i in range(len(points)-1):
                x=points[i+1][0]-points[i][0]
                y=points[i+1][1]-points[i][1]
                summ+=max(abs(x),abs(y))
        return summ 
        
        
        
        
        
        
        
        
        
        
        
        
                  # ans=0
                  # count=0
                  # for i in range(len(points)-1):
                  #       for j in range(len(points[0])-1):
                  #           if points[i][j]==points[i+1][j]:
                  #               ans+=points[i+1][j+1]-points[i][j+1]
                  #           elif points[i][j+1]==points[i+1][j+1]:
                  #               ans+=points[i][j]-points[i+1][j]
                  #           else:
                  #               ans+=abs(points[i+1][j+1]-points[i][j+1])
                  # return ans
                        
                        
                        
                        