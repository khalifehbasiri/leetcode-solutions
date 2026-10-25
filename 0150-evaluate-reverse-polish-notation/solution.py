class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": lambda a, b: int(a / b)
}


        stack = []
        for char in tokens:
            if char.lstrip('-').isdigit():
                if len(stack) >= 1:
                    f = stack[-1]
                    stack.append(int(char))
                    s = int(char)
                    
                else:
                    f = int(char)
                    stack.append(int(char))
                    
            else:
                print(char)
                s = ops[char](f, s)

                stack.pop()
                stack.pop()
                f = stack[-1] if len(stack) >= 1 else None
                stack.append(s)
        
        return stack[-1]
                
                
                