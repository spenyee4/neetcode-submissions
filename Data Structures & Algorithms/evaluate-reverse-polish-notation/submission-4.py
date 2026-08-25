class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operand = {'+':'+', '-':'-', '*':'*', '/':'/'}

        

        for token in tokens:
            if token not in operand:
                stack.append(int(token))
            else:
                if token == '+':
                    result = stack[-2] + stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(result)
                elif token == '-':
                    result = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(result)
                elif token == '*':
                    result = stack[-2] * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(result)
                elif token == '/':
                    result = int(float(stack[-2] / stack[-1]))
                    stack.pop()
                    stack.pop()
                    print(result)
                    stack.append(result)
                
        return stack[-1]