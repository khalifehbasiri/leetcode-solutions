class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[0:k])
        averages = [total]

        i = 1
        j = k

        while j < len(nums):
            total = total - nums[i-1] + nums[j]
            averages.append(total)
            i += 1
            j += 1
        return max(averages) / k