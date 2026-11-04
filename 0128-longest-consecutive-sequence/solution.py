class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sNums = set(nums)
        longestS = 0

        for num in sNums:
            if num - 1 not in sNums:
                length = 0

                while num + length in sNums:
                    length += 1
                
                longestS = max(longestS, length)
        
        return longestS
                







        