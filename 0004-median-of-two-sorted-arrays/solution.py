class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = sorted(nums1 + nums2)
        middle = len(nums) // 2
        
        return float(nums[middle]) if (len(nums) % 2 == 1) else (nums[middle - 1] + nums[middle]) / 2


