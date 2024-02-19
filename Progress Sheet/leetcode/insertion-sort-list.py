# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head 
        prevNode = None
        while current:
            nextNode = current.next
            current.next = prevNode
            if current.next and current.val > current.next.val:
                prevNode = current.next
            else:
                prevNode = current

            key = current.val
            temp = current
            while temp.next and key > temp.next.val:
                  temp = temp.next
            
            x = temp.next
            temp.next = current
            current.next = x
            current = nextNode
        return prevNode

       


        