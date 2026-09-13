class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        solution = {}
        
        for i, x in enumerate(nums):
            if target - x in solution:
                return [solution[target - x], i]
            solution[x] = i

        return []
