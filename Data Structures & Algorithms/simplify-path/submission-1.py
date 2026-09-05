class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")
        print(parts)
        for part in parts:  
            if part == "..":
                if stack:
                    stack.pop()
            elif part != "." and part != "":
                stack.append(part)
    
        return "/" + "/".join(stack)
        