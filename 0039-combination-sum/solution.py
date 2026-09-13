class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        temp = []
        
        def backtracking(index, remaining):
            if remaining == 0:
                output.append(temp.copy())
                return
            
            if remaining < 0 or index < 0:
                return
            
            temp.append(candidates[index])
            backtracking(index, remaining - candidates[index])
            
            temp.pop()
            
            backtracking(index-1, remaining)
        
        backtracking(len(candidates)-1, target)
        return output