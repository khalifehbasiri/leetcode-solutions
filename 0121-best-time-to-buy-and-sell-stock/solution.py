class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0

        left = 0
        right = 1
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right  
            else:
                current_max = prices[right] - prices[left] 
                max_profit = max(current_max, max_profit)

            right += 1
        
        return max_profit

        