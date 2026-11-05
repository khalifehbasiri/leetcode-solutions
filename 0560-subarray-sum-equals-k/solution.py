class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sums = {0: 1}

        TotalSum = 0
        currSum = 0
        for num in nums:
            currSum += num

            if currSum - k in sums:
                TotalSum += sums[currSum - k]

            if currSum in sums:
                sums[currSum] += 1
            else:
                sums[currSum] = 1
        
        return TotalSum

            
