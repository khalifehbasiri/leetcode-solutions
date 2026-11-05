class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "}": "{", "]": "["}

        for elem in s:
            if elem in brackets:
                last_elem = stack.pop() if stack else ""
                if brackets[elem] != last_elem:
                    return False
            else:
                stack.append(elem)
        
        return not stack

            


        