class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        i = 0
        while i < len(flowerbed):
            leftEmpty = i == 0 or flowerbed[i - 1] == 0
            rightEmpty = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

            if n > 0:
                if leftEmpty and flowerbed[i] == 0 and rightEmpty:
                    flowerbed[i] = 1
                    n -= 1
            i+=1

        return (n == 0)

                


