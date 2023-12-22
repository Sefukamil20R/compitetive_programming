class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans=[]
        temp=[]
        for x in image:
            x.reverse()
            print(x)
            for i in range(len(x)):
                if x[i]==0:
                    x[i]=1
                else:
                    x[i]=0
            temp.append(x)
        ans.extend(temp)
        return ans
        
            
           

        