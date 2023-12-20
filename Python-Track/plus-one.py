class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
            res=""
            r=""
            ans=[]
            for num in digits:
              res+=str(num)
            summ=int(res)+1
            r=str(summ)
            for i in range(len(r)):
                ans.append(int(r[i]))
            return ans
                