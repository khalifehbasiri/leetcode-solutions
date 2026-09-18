class Solution:
    def change(self, amount: int, coins: list[int]) -> int:

        cache = {}

        def countWays(target, i):
            if target == 0:
                return 1
            
            if target < 0 or i == len(coins):
                return 0

            if (target, i) in cache:
                return cache[(target, i)]
            
            useCoin = countWays(target - coins[i], i)

            skipCoin = countWays(target, i + 1)

            cache[(target, i)] = useCoin + skipCoin

            return cache[(target, i)]
        
        return countWays(amount, 0)