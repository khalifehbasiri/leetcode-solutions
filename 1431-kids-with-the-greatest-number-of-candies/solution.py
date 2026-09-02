class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        output = []
        gNum = max(candies)

        for candy in candies:
            output.append((candy + extraCandies) >= gNum)
        
        return output 