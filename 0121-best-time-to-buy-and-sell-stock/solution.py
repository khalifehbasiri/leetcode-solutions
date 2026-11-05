class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 1

        maxProfit = 0
        while left < right and right < len(prices):
            profit = prices[right] - prices[left]
            
            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                right += 1
            
            maxProfit = max(maxProfit, profit)
        
        return maxProfit