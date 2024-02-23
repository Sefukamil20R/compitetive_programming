class Solution:
    def bestClosingTime(self, customers: str) -> int:
        amount = 0
        maxx  , res = 0, 0
        for i , cust in enumerate(customers):
            if cust == "Y":
                amount += 1
            else:
                amount -= 1
            if amount > maxx:
                maxx = amount 
                res = i + 1
        return res 
             

        