class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        res = 0
        for i in range(len(s)):
            if s[i] == "(":
                open += 1
            else:
                if open != 0:
                    open -= 1
                else:
                    res += 1 #means i dont have opening so i need a parenthesis 
                    # to make valid parenthesis
        return res + open
        # the reason i add open is if there is a case where open parenthesis are at the 
        # end ma operations works if close so i wll add the left opens to make it valid

            
        