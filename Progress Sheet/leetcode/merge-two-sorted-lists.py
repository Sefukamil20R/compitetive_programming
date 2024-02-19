# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        # intialize dummy node with defualt value which is val = 0, next = none
        # purpuse is to handle the case when head is none that protect the run
        # time error when head.next is None at the first time
        head = dummyNode
        # we are intializing the head pointer to dummynode this head wil used 
        # merged linked list
        while list1 and list2: #while both list1 and list2 became none
          if list1.val < list2.val:
              head.next = list1 # setting nextnode of headpointer to list1
              list1 = list1.next
          else:
              head.next = list2
              list2 = list2.next
          head = head.next # in either case head will move to the nextnode
        if list1:
            head.next = list1 #if there is left node it will append atend of mergedlist
        if list2:
            head.next = list2
        return dummyNode.next
        # the reason we are returning dummy.nextnode is wea re aksed to return the
        # head of merged list since dummy.next if next node of dummy which is head 
        # but if we return head.next it will start form the second node of merged list
        # and if we return head which is last node of merged list as we are going until the list1 and list2 became none 
        # if we return head.next instead of dummy.next,
        # the head would be pointing to the dummy node initially. Therefore,
        # returning head.next would effectively return the s
        # econd node of the merged list, skipping the first node, which is the dummy node.   
        #dummy.next, we ensure that we return the correct starting point of the
        #  merged list, which includes all the nodes starting from the first 
        #  actual node, not skipping any nodes. 