class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        max_ind=0
        one=0
        for i in flips:#for every iteration one is added
            one+=1
            max_ind = max (max_ind,i)
            if max_ind == one:
                count += 1
        return count

    
        
           

                 


        