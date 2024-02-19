# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
         fast = head
         slow = head
          #  after this loop slow is starts from the middle of the loop
         while fast and fast.next:
             slow = slow.next
             fast = fast.next.next
         prevNode = None 
        #  the following loop is for reversing the pointers 
         while slow:
            nextNode = slow.next
            slow.next = prevNode
            prevNode = slow 
            slow = nextNode
         temp= head
         while prevNode:
             if temp.val != prevNode.val:
                 return  False
             else:
                 prevNode =  prevNode.next
                 temp = temp.next
         return  True
            

