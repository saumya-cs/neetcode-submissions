class Solution:
    def isValid(self, s: str) -> bool:
        mappedParentheses = {"(":")", "[":"]", "{":"}"}
        stack = []
        for i in range(len(s)):
            if(s[i] == "(" or s[i] == "[" or s[i] == "{"):
                stack.append(mappedParentheses[s[i]])
            else:
                if (stack and stack[-1] == s[i]):
                    stack.pop()
                else:
                    return False
        if(not stack): return True
        return False
