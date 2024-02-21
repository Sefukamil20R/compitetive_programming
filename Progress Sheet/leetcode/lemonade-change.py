class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = defaultdict(int)
        for i in range(len(bills)):
            if bills[i] == 5:
                  count[bills[i]] += 1
            elif bills[i] == 10 and (count[5]):
                count[bills[i]] += 1
                count[5] -= 1
                
            elif  bills[i] == 20 and ((count[10]and count[5]) or count[5] >= 3 ):
                
                if count[10] and count[5]:
                    count[10] -=1
                    count[5] -= 1 
                else:
                    count[5] -= 3
                 
                # if we cannot enter into if and elif this means we cannot make the above operation 
                # which makes it false
            else:
                return False 
        return True
        # but in the loop if we can break the loop with out getting else which is we can 
        # make the operations which make it true

                    

        