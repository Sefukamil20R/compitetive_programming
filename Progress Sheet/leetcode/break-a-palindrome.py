class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        lists = list(palindrome)
        count = 0
        n =len(lists)
        if len(lists) == 1:
            return ""
        for i in range(len(lists)):
            if i == n//2:
               continue
            if lists[i] != "a":
                lists[i] = "a"
                return "".join(lists)
        lists[-1] = "b"
        return "".join(lists)
        
        



        