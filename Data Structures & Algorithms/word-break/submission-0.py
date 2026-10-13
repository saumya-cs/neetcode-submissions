class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        canSeparate = [False] * (len(s) + 1)
        #canSeparate[i] = if first i chars of s can break into wordDict
        canSeparate[0] = True
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if canSeparate[j] and s[j:i] in wordDict:
                    canSeparate[i] = True
                    break
        return canSeparate[-1]