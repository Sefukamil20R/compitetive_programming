class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
          deck.sort()
          que = deque()
          for i in range(len(deck)-1,-1,-1):
              if que:
                  val = que.pop()
                  que.appendleft(val)
              que.appendleft(deck[i])
          return que