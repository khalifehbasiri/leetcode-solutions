class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        target = len(nums) - 1
        
        for i, x in enumerate(nums):
            if reach >= target:
                return True
                
            if i > reach:
                return False
            
            if i + x > reach:
                reach = i + x
        return False