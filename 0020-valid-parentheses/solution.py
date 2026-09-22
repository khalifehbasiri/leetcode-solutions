class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in brackets:
                top_char = stack.pop() if stack else ""
                if top_char != brackets[char]:
                    return False
            else: 
                stack.append(char)
        
        return not stack