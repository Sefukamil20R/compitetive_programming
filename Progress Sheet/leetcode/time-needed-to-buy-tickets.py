class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        que = deque()
        for i in range(len(tickets)):
            que.append(i)
        print(que)
        while (tickets[k]!=0):
            val = que.popleft()
            time += 1
            tickets[val] -= 1
            if tickets[val] !=0:
               que.append(val)
           
        return time
        



        