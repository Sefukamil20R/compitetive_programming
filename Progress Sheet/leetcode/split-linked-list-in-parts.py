# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
             current = head
             count = 0 
             res = [None]*k
             while current:
                 count += 1
                 current = current.next
             add = count//k
             mod = count % k
             i = 0
             while head:
                 j = 0
                 store = head
                 while head and j < (add + (i<mod)-1):
                      head = head.next
                      j += 1
                 current = head.next
                 if head:
                     head.next = None

                 head = current
                 res[i] = store
                 i += 1
             return res


             
             









 