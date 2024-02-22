class doublelinked:
    def __init__(self,val = " ",next = None , prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = doublelinked(homepage, None, None)
        # homepage is set its next and prev none
        self.current = self.head
        # intializing our head to current which is used for traversing
        

    def visit(self, url: str) -> None:
        curr = doublelinked(url, None, self.current)
        # curr is our new node
        self.current.next = curr
        # current is our pointer which was previously pointing to head
        # but now so it is pointing to new  curr node
        self.current = curr
        # then we are updating our current pointer to go to our new node so
        # we rae updating our current poin(moving to next nodes)
        

    def back(self, steps: int) -> str:
        while self.current.prev and steps:
            self.current = self.current.prev
            steps -= 1
        return self.current.val 
        # when we get last node we have to return it 
        

    def forward(self, steps: int) -> str:
        while self.current.next and steps:
            self.current = self.current.next
            steps -= 1
        return self.current.val 
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)