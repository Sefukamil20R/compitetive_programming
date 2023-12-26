class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=len(names)
        for i in range(n):
            cur=i
            for j in range (i+1,n):
                if heights[j] > heights[cur]:
                    cur=j
            if cur != i:
                 heights[i],heights[cur] =heights[cur],heights[i]
                 names[i],names[cur] =names[cur],names[i]
        return names

        # insertion sort
        # for i in range (len(names)-1):
        #     for j in range(len(heights)-1):
        #         if heights[j] < heights[j+1]:
        #             heights[j],heights[j+1] =heights[j+1],heights[j]
        #             names[j],names[j+1] =names[j+1],names[j]
        # return names 

            
        