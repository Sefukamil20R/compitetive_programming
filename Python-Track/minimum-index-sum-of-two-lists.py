

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dis = {}
        min_idx = float("inf")
        res = []

        for i in range(len(list1)):
            dis[list1[i]] = i

        for i in range(len(list2)):
            if list2[i] in dis:
                idx = dis[list2[i]] + i
                if idx < min_idx:
                    min_idx = idx
                    res = [list2[i]]
                elif idx == min_idx:
                    res.append(list2[i])

        return res
