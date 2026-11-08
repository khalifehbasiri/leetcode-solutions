class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        
        taxToPay = 0
        upper = 0
        while income > 0 and upper < len(brackets):
            if upper > 0:
                if (income - (brackets[upper][0] - brackets[upper - 1][0])) >= 0:
                    taxToPay += (brackets[upper][0] - brackets[upper - 1][0]) * (brackets[upper][1] / 100)
                    income -= (brackets[upper][0] - brackets[upper - 1][0])
                else:
                    taxToPay += (income) * (brackets[upper][1] / 100)
                    income -= (brackets[upper][0] - brackets[upper - 1][0])
                    
            else:
                if (income - brackets[upper][0]) >= 0:
                    taxToPay += (brackets[upper][0]) * (brackets[upper][1] / 100)
                    income -= brackets[upper][0]
                else:
                    taxToPay += (income) * (brackets[upper][1] / 100)
                    income -= brackets[upper][0]
            upper += 1

        return taxToPay
