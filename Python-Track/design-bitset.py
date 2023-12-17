class Bitset:

    def __init__(self, size: int):
        self.n=size
        self.flipped=False
        self.total=0
        self.seen=defaultdict(int)
        
    def fix(self, idx: int) -> None:
        prev=self.seen[idx]
        if self.flipped:
            self.seen[idx]=0
            if prev!=0:
                self.total-=1
        else:
            self.seen[idx]=1
            if prev!=1:
                self.total+=1
                
                
    def unfix(self, idx: int) -> None:
        prev=self.seen[idx]
        if self.flipped:
            self.seen[idx]=1
            if prev!=1:
                self.total+=1
        else:
            self.seen[idx]=0
            if prev!=0:
                self.total-=1
                
        
        

    def flip(self) -> None:
        self.flipped= not self.flipped
        

    def all(self) -> bool:
         if self.flipped:
            return self.total==0
         else:
            return self.total == self.n 
        
        

    def one(self) -> bool:
         if self.flipped:
            return self.total < self.n 
         else:
                return self.total>0
            
        
        

    def count(self) -> int:
        if self.flipped:
            return self.n - self.total
        else:
                return self.total
            
        
        

    def toString(self) -> str:
        res=[]
        for i in range(self.n):
            a=self.seen[i]
            if self.flipped:
                 a=1-a
            res.append(a)

        return "".join(str(x) for x in res)
                    
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()