class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = sum(nums[0:k])
        max_total = sums

        i = 1
        j = k

        while j < len(nums):
            sums = sums - nums[i-1] + nums[j]
            max_total = sums if sums > max_total else max_total
            i += 1
            j += 1
        return max_total / k