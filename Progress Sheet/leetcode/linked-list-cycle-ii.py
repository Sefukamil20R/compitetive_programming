# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # in order to return node when cycle begins first we have to if there 
        # is a cycle in LL
        fast = head
        slow = head
        while fast and fast.next:
            # as fast is going twice as slow it will reach the end first 
            # so we are checking if fast.next.next is not none
            # This condition ensures that we can move fast two steps ahead without 
            # encountering a null pointer, preventing null pointer errors
            #  when accessing fast.next.next.
            fast = fast.next.next
            slow = slow.next
            if fast == slow: #checking if there is a cycle
                while head != slow: #check when head and slow meets 
                        slow = slow.next
                        head = head.next
        # we start moving slow pointer at meeting and head from the begning of LL
                return head
        return None
        
