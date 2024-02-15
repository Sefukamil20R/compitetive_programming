# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val 
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
       fast = head
       slow = head 
    #    as the fast moves twice than the slow when fast gets at the end or 
    #    becomes none slow becomes at halfway so slow became athe middle node 
       while fast and fast.next:
           fast = fast.next.next
           slow = slow.next
       return slow          
      