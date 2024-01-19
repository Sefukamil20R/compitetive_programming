class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*(n+1)
        for lb , rb , seat in bookings:
            res[lb - 1] += seat
            res[rb] -= seat
        total = 0
        prefix = []
        for i in range(len(res)):
            total += res[i]
            prefix.append(total)
        prefix.pop()
        return prefix


        