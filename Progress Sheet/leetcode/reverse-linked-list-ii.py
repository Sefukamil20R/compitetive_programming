# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
           DummyNode = ListNode()
        #  connecting this dummynode with head
           DummyNode.next = head
           lefter = DummyNode 
        #    lefter is used to store nodes before left pointer
           for i in range (left -1):#pointers are 1 indexed in this 
              lefter = lefter.next
           leftNode = lefter.next 
        #    leftNode is the node where left starts
           fisrtleft = leftNode
        #    storing the node of left starts that will used to merge  
        #   after the LL is reversed 
           prevNode = None
           for j in range(right - left + 1):
               nextNode = leftNode.next
               leftNode.next = prevNode
               prevNode = leftNode
               leftNode = nextNode
            #    above loop is for revering the LL from left to right
           lefter.next = prevNode
        #    starts merging lefter(beforeleft) to reversed part which starts 
        # from prevnode 
           fisrtleft.next = leftNode
        #  after the reversed part first left which now set to be at the final 
        # reversed LL then it has to linked with the lists after Reversed LL so
        # leftNode is at the last of LL so fisrtLrft starts points to LeftNode 
           return DummyNode.next 
        #    skiiping the dummp part





