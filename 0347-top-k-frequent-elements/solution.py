class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        largest = [[] for _ in range(len(nums)+1)]
        max = []

        
        for i, x in enumerate(nums):
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
                
        for val in counts:
            if largest[counts[val]] == []:
                largest[counts[val]] = [val]
            else:
                largest[counts[val]].append(val)
        
        for j in range(len(largest)-1, -1, -1):
            for num in largest[j]:
                max.append(num)
                if len(max) == k:
                    return max
            
        return max