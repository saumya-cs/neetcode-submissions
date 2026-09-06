class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = 0
        while (idx < len(strs[0])):
            letter = strs[0][idx]
            for i in range(1, len(strs)):
                word = strs[i]
                if idx >= len(word) or word[idx] != letter:
                    return strs[0][:idx]
            idx += 1
        return ""

        