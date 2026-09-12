class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
            
        nums = sign * int(str(abs(x))[::-1])
        
        if nums < -(2**31) or nums > 2**31 - 1:
            return 0
        
        return nums