class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        SortNums = sorted(nums1+nums2)

        if len(SortNums) % 2 != 0:
            return SortNums[len(SortNums) // 2]
        else:
            return (SortNums[len(SortNums) // 2 - 1] + SortNums[len(SortNums) // 2]) / 2