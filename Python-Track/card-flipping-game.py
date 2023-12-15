class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same=set()
        for f,b in zip(fronts,backs):
            if f==b:
                same.add(f)
        print(list(zip(fronts,backs)))
        can=set()
        for f,b in zip(fronts,backs):
            if f  not in same:
                can.add(f)
            if b  not in same:
                can.add(b)
        if not can:
            return 0
        return min(can)
            
                
            