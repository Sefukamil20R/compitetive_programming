# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
          DummyNode = ListNode(0 , head ) # dummynode points to head of original LL
       
          leftpoin = DummyNode # leftpoin points to DummyNode
           #   used to traverse for orignal LL starts from DummyNode
          right = head #used for traversing original LL
          while n > 0 and right:
            # right will does through n size 
            right = right.next
            n -= 1
            # the following loop starts after above so 
            # right will continue from end of above loop
            # initially, right was moved n positions ahead of left, 
            # so it starts from the node n positions ahead of left.
          while right:
              right = right.next
              leftpoin = leftpoin.next
            #   left will be at postion at before the removable node 
          leftpoin.next = leftpoin.next.next 
        #   skipping the removable node 
          return DummyNode.next
        #    as DummyNode,next is second node of modified node as the first node is dummy

