class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        strs = ""
        new_dic = dict(zip(indices,s))
        new_dic = dict(sorted(new_dic.items()))
        for value in new_dic.values():
            strs+=value
        return strs
            