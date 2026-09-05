class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ""
   
        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == '[':
                # Push the full number onto the stack, then push '['
                stack.append(curr_num)
                stack.append('[')
                curr_num = 0
            elif c == ']':
                currStack = []
                while stack and stack[-1] != '[':
                    currStack.append(stack.pop())
                stack.pop()
                num = stack.pop()
                for i in range(num):
                    for i in range(len(currStack)-1, -1, -1):
                        stack.append(currStack[i])
                        
            else:
                stack.append(c)
        return "".join(stack)
            
        