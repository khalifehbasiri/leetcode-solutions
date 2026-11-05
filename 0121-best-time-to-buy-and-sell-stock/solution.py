class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 1

        maxProfit = 0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            
            right += 1
        return maxProfit