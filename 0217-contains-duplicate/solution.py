class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dupe = {}
        
        for x in nums:
            if x in dupe:
                return True
            dupe[x] = 1
        
        return False