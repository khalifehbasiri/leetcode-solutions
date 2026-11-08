class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:

        taxed = 0

        upper = 0
        while income > 0:
            if upper > 0:
                bracketSize = brackets[upper][0] - brackets[upper - 1][0]
            else:
                bracketSize = brackets[upper][0]
            taxableIncome = min(income, bracketSize) 
            taxRate = brackets[upper][1] / 100

            taxed += taxableIncome * taxRate
            income -= taxableIncome
            upper += 1
        
        return taxed




