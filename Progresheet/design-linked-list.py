class Node:
  def __init__(self , value = 0):
  
    self.value = value
    self.next = None

    
      

  



class MyLinkedList:

    def __init__(self):
        self.head = Node()
        # object creation
        

    def get(self, index: int) -> int:
        index += 1
        # this is done coz the actual counting starts from dummy headnode
        # but when user enter 0 means they want to consider the actual firts node so 
        # to pass the dummy node we have to increment it 
        temp = self.head
        for _ in range(index):
            if temp == None:
                return -1
            temp = temp.next
        if temp == None:
            return -1
        return temp.value
        

    def addAtHead(self, val: int) -> None:
       self.addAtIndex(0 , val)


        

    def addAtTail(self, val: int) -> None:
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        temp.next = Node(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        temp = self.head
        for _ in range(index):
              if temp == None:
                return 
              temp = temp.next
        if temp == None:
                return 
        newnode = Node(val)
        newnode.next = temp.next
        temp.next = newnode

        


    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        for _ in range(index):
             if temp == None:
                return 
             temp = temp.next
        if temp == None:
                return 
        if temp.next:
            temp.next = temp.next.next
         


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)