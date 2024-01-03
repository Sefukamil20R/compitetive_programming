class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        horiz = []
        maxx = 0
        for i , j in points:
            horiz.append(i)
        print(horiz)
        horiz.sort()
        print(horiz)
        for i in range (len(horiz)-1):
            maxx = max(maxx , abs(horiz[i]-horiz[i+1]))
        return maxx


        