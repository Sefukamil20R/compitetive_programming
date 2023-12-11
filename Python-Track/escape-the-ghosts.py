class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        disor =abs(target[0])+abs(target[1])
        for ghost in ghosts:
            dis = abs(target[0]-ghost[0])+ abs(target[1]-ghost[1])
            if dis <= disor:
                return False
        return True 
