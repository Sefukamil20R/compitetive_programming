class OrderedStream:

    def __init__(self, n: int):
        self.list=[None]*(n+1)
        self.ptr=1
        
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.list[idKey]=value
        ans=[]
        while self.ptr < len(self.list) and self.list[self.ptr]is not None:
            
            ans.append(self.list[self.ptr])
            self.ptr+=1
        return ans
            
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)