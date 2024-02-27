class Solution:
    def decodeString(self, s: str) -> str:
         
        def decode(l,r):
           
            si = -1
            dig = ""
            ans =  ""
            ob = 0
            for i in range(l, r):
                if s[i].isdigit() and ob == 0:
                    dig += s[i]
                elif s[i] == "[" :
                    if ob == 0:
                        si = i
                         
                    ob += 1
                elif s[i] == "]":
                    ob -= 1
                    if ob == 0:
                        ans +=  int(dig) * decode(si + 1,i)
                        dig = ""
                elif ob == 0 :
                    ans += s[i]

            return ans
            
        return decode(0,len(s))
            

                   