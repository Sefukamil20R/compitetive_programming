
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next

            fast = fast.next.next
            if slow == fast:
                return True
            # if there is no cycle in the linkedlist fast will be go to none 
            # but if there is cycle as fast is moving twice as slow will be equal to slow 
            # back with out getting none 
          
        return False 

        