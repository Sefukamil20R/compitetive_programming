class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count=Counter(arr1)
        ans=[]
        temp=[]
        for i in range(len(arr2)):
            ans.extend([arr2[i]]*count[arr2[i]])
        
        for i in range (len(arr1)):
            if arr1[i] not in ans:
                temp.append(arr1[i])
        temp.sort()
        ans.extend(temp)
        return ans
        
        #  count={}
        #  ans=[]
        #  for i in range(len(arr2)):
        #      count[arr2[i]]=i
        #  print(count)
        #  arr1.sort()
        #  print(arr1)
         
        
             
             
             
