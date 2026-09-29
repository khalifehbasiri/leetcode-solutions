class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0

        left = 0
        right = 1
        while left < right and right < len(prices):
            if prices[left] > prices[right]:
                left = right
                right = left + 1
                continue

            current_max = prices[right] - prices[left] 
            
            if current_max > max_profit:
                max_profit = current_max 

            right += 1
        
        return max_profit

        