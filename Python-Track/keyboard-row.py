class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1=set("qwertyuiop")
        set2=set("asdfghjkl")
        set3=set("zxcvbnm")
        res=[]
        for i in range(len(words)):
            new_set=set()
            for j in range(len(words[i])):
                if words[i][j].lower() in set1:
                    new_set.add(1)
                elif  words[i][j].lower() in set2:
                    new_set.add(2)
                else:
                    new_set.add(3)
            if len(new_set)==1:
                res.append(words[i])
        return res
        
                
                    
                    
       
        