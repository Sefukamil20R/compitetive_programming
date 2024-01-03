class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
         skill.sort()
         print(skill)
         l , r = 0 , len(skill)-1
         n = len(skill)
         summ = skill[l] + skill[r]
         res = 0
         while l < r:
                if skill[l] + skill[r] == summ:
                   res += (skill[l]*skill[r])
                   l += 1
                   r -= 1
                else :
                    return -1
         return res
        