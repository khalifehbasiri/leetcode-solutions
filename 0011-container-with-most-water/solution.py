class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1

        maxA = 0
        while left < right:
            area = min(height[left], height[right]) * abs(left - right)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            maxA = max(maxA, area)
        
        return maxA







        