class Solution:
 def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
            # if their length is less than 2 means the string doesnot have 
            # small or upper case so it is base case 
        s_set = set(s)
        
        for i,c in enumerate(s):
            if c.swapcase() not in s_set:
                s1 = self.longestNiceSubstring(s[0:i])
                #  yaz , aAaY
                # aAa Y
                # output = aAy
                s2 = self.longestNiceSubstring(s[i+1:])
                
                return s2 if len(s2) > len(s1) else s1
                #  if both strings are nice will return s1 otherwise will return 
                # longest one 
        return s
        # if we dont get a letter doesnot have swapcase in its substring 
        # it means the whole string is nice so we willreturn s
        