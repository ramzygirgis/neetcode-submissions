class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['+', '-', '*', '/']
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in operands:
                int2 = int(stack[-1]) # double check later
                int1 = int(stack[-2]) # double check later
                if tokens[i] == '+':
                    result = int1 + int2
                if tokens[i] == '-':
                    result = int1 - int2
                if tokens[i] == '*':
                    result = int1 * int2
                if tokens[i] == '/':
                    result = int1 / int2 
                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                stack.append(tokens[i])
        return int(stack[0])