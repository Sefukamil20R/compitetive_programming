class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        arr = [0]*len(s)
        for i in range(len(s)):
            word = s[i][:-1]
            index = int(s[i][-1])
            arr[index-1] = word

        return ' '.join(arr)