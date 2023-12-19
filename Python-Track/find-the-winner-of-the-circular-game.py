class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[i for i in range(1,n+1)]
        print(arr)
        i=0
        k-=1
        while (n>1) :
            arr.pop((i+k)%n)
            i=(i+k)%n
            n-=1
        return arr[0]
        
            
           
           
            
            
            
            
           
        
        