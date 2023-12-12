class Solution:
    def reverseWords(self, s: str) -> str:
          lists=s.split()
          print(lists)
          res=[]
          for i in range(len(lists)-1,-1,-1):
                res.append(lists[i])
          return " ".join(res)

        
        