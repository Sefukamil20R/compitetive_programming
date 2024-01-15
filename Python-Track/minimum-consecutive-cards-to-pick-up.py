class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        minn = float("inf")
        seen = {}
        for i in range(len(cards)):
            if cards[i] in seen:
                 minn = min(minn , i - seen[cards[i]]+1)
            seen[cards[i]] = i
        return minn if minn != float("inf") else -1

            

                
        