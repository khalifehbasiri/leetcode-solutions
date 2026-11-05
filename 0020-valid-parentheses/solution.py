class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for elem in s:
                if stack and elem == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif stack and elem == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                elif stack and elem == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                else:  
                    stack.append(elem)
        
        return not stack

            


        