class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t == '+':
                one = stack.pop()
                two = stack.pop()
                stack.append(one + two)
            elif t == '-':
                one = stack.pop()
                two = stack.pop()
                stack.append(one - two)
            elif t == '*':
                one = stack.pop()
                two = stack.pop()
                stack.append(one * two)
            elif t == '/':
                one = stack.pop()
                two = stack.pop()
                stack.append(one // two)
            else:
                stack.append(int(t))
        return stack[-1]
           

            
        