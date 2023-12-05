class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
            concat1=""
            concat2=""
            for strs1 in word1:
                 concat1+=strs1
            for strs2 in word2:
                 concat2+=strs2
            return concat1==concat2
            
            
            
                