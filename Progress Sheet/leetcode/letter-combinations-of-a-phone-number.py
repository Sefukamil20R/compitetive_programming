class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        store = {
             "2" : "abc",
             "3" : "def",
             "4" : "ghi",
             "5" : "jkl",
             "6" : "mno",
             "7" : "pqrs",
             "8" : "tuv",
             "9" : "wxyz"
        }
        ans = []
        path = []
        if digits == "":
            return []
        def back(idx):
            nonlocal path
            if len(path) == len(digits):
                ans.append("".join(path[:]))
                return 
            
            val = store[digits[idx]]
            for char in val:
                path .append(char) 
                back(idx+1)
                path.pop()
        back(0)
        return ans





        



        