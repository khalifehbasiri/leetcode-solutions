class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count("Y")
        min_panalty = penalty
        best_hour = 0

        for i, customer in enumerate(customers):
            if customer == "Y":
                penalty -= 1
            else:
                penalty += 1
            
            if penalty < min_panalty:
                min_panalty = penalty
                best_hour = i + 1
        
        return best_hour
