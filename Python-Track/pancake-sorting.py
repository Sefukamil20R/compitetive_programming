class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range (len(arr)):
            maxx = max(arr[:len(arr)-i])
            ind = arr[:len(arr)-i].index(maxx)
            arr[:ind+1] = arr[:ind + 1][::-1]
            ans.append(ind + 1)
            arr[:len(arr)-i] = arr[:len(arr)-i][::-1]
            ans.append(len(arr)-i)
        return ans

