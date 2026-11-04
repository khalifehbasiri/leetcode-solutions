class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = ((left + right) // 2)
            print("left: ", left)
            print("right: ", right)
            print("middle: ", middle)
            print("")

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        
        print("left: ", left)
        print("right: ", right)
        print("middle: ", middle)
        
        return -1
