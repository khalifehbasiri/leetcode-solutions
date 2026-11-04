class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sNums = set(nums)
        longestS = 0

        for num in sNums:
            curr = num
            if num - 1 not in sNums:
                length = 1

                while num + 1 in sNums:
                    num += 1
                    length += 1
                
                longestS = max(longestS, length)
        
        return longestS
                







        