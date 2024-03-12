class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire = deque()
        rad = deque()
        n = len(senate)
        for i in range(n):
            if senate[i] == "R":
                rad.append(i)
            else:
                dire.append(i)
        while dire and rad:
            d = dire.popleft()
            r = rad.popleft()
            if d < r:
                dire.append(n)
            else:
                rad.append(n)
            n += 1
        return "Dire" if dire else "Radiant"