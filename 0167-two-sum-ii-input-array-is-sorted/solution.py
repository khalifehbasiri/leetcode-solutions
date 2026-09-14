class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        num1 = 0
        num2 = 0
        while i < j:
            if numbers[i] + numbers[j] == target:
                num1 = i
                num2 = j
                break
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

        num1 += 1
        num2 += 1
        return [num1, num2]
            


        
            
