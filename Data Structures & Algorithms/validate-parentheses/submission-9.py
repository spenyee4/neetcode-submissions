class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        parenthesis = { '(' : ')', '[':']', '{':'}'}

        if len(s) < 2:
            return False

        for char in s:
            if char in parenthesis:
                stack.append(char)
            
            else:
                if stack and parenthesis[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True