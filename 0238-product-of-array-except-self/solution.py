class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = [1] * len(nums)

        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            answer[i] = prefix
            prefix = prefix * nums[i]
            i+=1
        
        i = len(nums) - 1
        while i >= 0:
            answer[i] *= suffix
            suffix = suffix * nums[i]
            i-=1

        return answer
