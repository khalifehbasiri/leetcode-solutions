class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sol = {}

        for i, x in enumerate(nums):
            if target - x in sol:
                return [sol[target - x], i]
            sol[x] = i
        
        return []
        