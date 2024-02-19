# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
            leftNode = ListNode()
            # intialized LL with dummy node used to partion LL having
            #  values less than x 
            # purpuse of having dummynode to access next pointerLL has to 
            # intializd with dummynode because if it is not intialized 
            # left will be None so next attribute cannot be accessed with
            # None doesnot have next attribute so it is to prevent attribute error
            leftPoin = leftNode 
            # leftpoin points to dummy node of leftNode LL
            rightNode = ListNode()
            # intialized LL with dummyNode used to partion LL having 
            # values greater than or equal to x
            rightPoin = rightNode
            # rightpoin points to dummynode of rightNode 
            current = head 
            # current is used to traverse over the original given LL
            while current: 
             # The loop continues as long as there are nodes
             # remaining in the original linked list (current is not None)
              if current.val < x :
                  leftPoin.next = current
                # our leftpoin stop to point dummy node then points to current
                # value is lessthan x
                  leftPoin = leftPoin.next
                #   moving our pointer to the next
                
              else:
                  rightPoin.next = current
                  # our rightpoin stop to point dummy node then points to current
                # value is greaterthan or equal to  x
                  rightPoin = rightPoin.next

              current = current.next
            leftPoin.next = None
            rightPoin.next = None
            # terminates the partitions by ensuring that the next node 
            # after the last node in each partition is None.means to prevent 
            # if there is a cycle in LL 
            # By setting the next pointers of the last nodes in both partitions to None, 
            # we ensure that no additional nodes are inadvertently included in 
            # the merged linked list during the merging process.
            leftPoin.next = rightNode.next
            # we are merging the two LL by setting the last pointer of leftpointer
            # to  starting node of the rightNOde rightnode.next is pointing to 
            # secondnode of righnode LL which is after dummynode
            return leftNode.next
            # we are returning the second pointer of the leftNode as the first  
            #  is dummynode the secod node is the actual part of LL
            # Finally, the method returns the head of the modified linked list,
            #  which starts from the second node of the left partition.
            #  This is because the first node in the left partition (left) is a
            #  dummy node, so we return its next node.
            
              
            

