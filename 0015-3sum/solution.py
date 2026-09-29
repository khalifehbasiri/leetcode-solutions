class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_num = sorted(nums)
        
        i = 0
        output = []
        while i < len(sorted_num) - 2:
            if sorted_num[i] > 0:
                break
                
            if i > 0 and sorted_num[i] == sorted_num[i - 1]:
                i += 1
                continue
                
            left = i + 1
            right = len(sorted_num) - 1
                
            while left < right:
                total = (
                    sorted_num[i] 
                    + sorted_num[left] 
                    + sorted_num[right]
                )
                
                if total < 0:
                    left += 1
                    
                elif total > 0:
                    right -= 1
                    
                else:
                    output.append([
                        sorted_num[i],
                        sorted_num[left],
                        sorted_num[right]
                    ])

                    left += 1
                    right -= 1

                    while left < right and sorted_num[left] == sorted_num[left - 1]:
                        left += 1

                    while left < right and sorted_num[right] == sorted_num[right + 1]:
                        right -= 1
            
            i += 1
        
        return output