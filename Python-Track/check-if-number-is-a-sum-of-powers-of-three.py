class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        counter=[]
        while n>=0:
            num=n
            count=0
            while (num >=3):
                count+=1
                num//=3
            num=n
            if count in counter:
                    num-=pow(3,count-1)
            else:
                    num-=pow(3,count)
                    counter.append(count)
            if num==0:
                    return True
            n=num
        return False
             
            
                