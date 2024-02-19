
class RecentCounter:
  def __init__(self):
      self.count = 0 #to count the number of requests 
      self.que = deque() # to store the timestamps 
    #   deque allows deleting and addind in both side
 
  def ping(self, t: int) -> int:
      self.que.append(t)
    #   each time the current timestamp is append to queue
      while self.que[0] < t - 3000:
        #   checking if firststamp in queue is older than 3000sec 
          self.que.popleft() # if it is we remove it 
          self.count -= 1
      return len(self.que) # length is number of request in deque

    
     
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)










   
   
   
   
   
   
    #  self.q=deque()
    #  self.count=0
    #   self.q.append(t)
    #   self.count+=1
    #   while self.q and self.q[0]<t-3000:
    #       self.q.popleft()
    #       self.count-=1
    #   return self.count



 # def __init__(self):
    #    self.q=collections.deque() 

    # def ping(self, t: int) -> int:
    #     self.q.append(t)
    #     while self.q[0]<t-3000:
    #         self.q.popleft()
    #     return len(self.q)