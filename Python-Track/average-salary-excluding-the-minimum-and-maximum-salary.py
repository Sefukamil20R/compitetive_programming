class Solution:
    def average(self, salary: List[int]) -> float:
        total=sum(salary)-min(salary)-max(salary)
        n=len(salary)-2
        return total/n