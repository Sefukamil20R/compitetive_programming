class Solution:
    def smallestNumber(self, num: int) -> int:
        zeros = 0
        n=str(num)
        if num > 0:
            num=list(map(int,n))
            print (num)
            num.sort()
            for i in range (len(num)):
                if num[i] == 0:
                    zeros += 1
                else:
                    break
            num[zeros] , num[0] = num[0]  , num[zeros] 
            print(n)
            final = list(map(str,num))
            return int("".join(final))
        elif num < 0 :
            num = list (map (int,n[1:] ))
            print(num)
            num.sort(reverse = True )
            final = list(map(str,num))
            return - int ("".join(final))
        else:
            return 0

            


            

            

        