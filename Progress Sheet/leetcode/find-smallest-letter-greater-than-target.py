class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left  , right = -1 , len(letters)-1
        while left + 1 < right:
            mid =  (left + right)// 2
            if letters[mid] > target:
                right = mid
            
            else:
                left = mid
        
        if letters[right] <= target:
            return letters[0]
        else:
            return letters[right] 