# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odds = head # odds points to orginalist head(first-node)
        evens = odds.next # evens points to second node of original list
        evenslist = evens #starts from second node the purse is after separating 
        # odds from evens to connect last odd index with the first evenindex 
        while evens and evens.next:#we have to check at least thre is 2 more node
        # after the current node we might miss processing the
        #  last odd node if it doesn't have a corresponding even node following it. 
        # malet enens bcha check karegn next malet oddun miss silemnareg
        # bcha bachru even hulete malet mehal lay odd silale hulete ew eyezelel mihedew 
        # so even and even.next sinil we can move even hulete kezi buhala with out
        # encountering none malet so even.next.next none endalhone check eyaregn new 
            odds.next = evens.next
            odds = odds.next 
            evens.next = odds.next
            evens = evens.next
        odds.next = evenslist # as we stored the fisrt even number in the evenlist then 
        # after we collect all odds in the loop we will link the fisrt even to the odds next
        return head

    
       

        
