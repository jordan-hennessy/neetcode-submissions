class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operands = ('+', '-', '*', '/')

        stack = []

        for i in tokens:

            if i in operands:

                if i == '+':
                    b = stack[-1]
                    stack.pop()

                    a = stack[-1]
                    stack.pop()

                    c = a + b
                    stack.append(c)

                elif i == '-':
                    b = stack[-1]
                    stack.pop()

                    a = stack[-1]
                    stack.pop()

                    c = a - b
                    stack.append(c)

                elif i == '*':
                    b = stack[-1]
                    stack.pop()

                    a = stack[-1]
                    stack.pop()

                    c = a * b
                    stack.append(c)

                elif i == '/':
                    b = stack[-1]
                    stack.pop()

                    a = stack[-1]
                    stack.pop()

                    c = a / b
                    stack.append(int(c))

            else:
                stack.append(int(i))

        return int(stack[-1])