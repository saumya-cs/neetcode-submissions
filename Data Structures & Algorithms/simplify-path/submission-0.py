class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")
        print(parts)
        for part in parts:
            if part == ".":
                stack.append("/")
            elif part == ".." and stack:
                stack.pop()
                if stack:
                    stack.pop()
            elif part == "":
                if stack:
                    if stack[-1] != "/":
                        stack.append("/")
                else:
                    stack.append("/")

                
            else:
                stack.append(part)
                stack.append("/")
        if stack and len(stack) > 1:
            stack.pop()
        return "".join(stack)
        