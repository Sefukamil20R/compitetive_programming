class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 1
        points.sort(key = lambda x : x[1])
        print(points)
        i = 0
        for j in range(1 ,len(points)):
            if points[i][1]  < points[j][0]:
                count += 1
            
                i = j
        return count 




















        # for i in range(len(points)):
        #     for j in range(len(points[0])):
        #         if points[i][1] <= points[i + 1][1]:
        #                if points[i][1] >= points[i + 1][0]




        