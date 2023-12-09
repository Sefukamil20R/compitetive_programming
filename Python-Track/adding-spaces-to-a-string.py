class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
                strs=""
                space=set(spaces)
                for i in range(len(s)):
                    if i in space:
                        strs+=" "
                    strs+=s[i]
                return strs
           
             
        
    