class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        
        for i in range(len(word1)):
            result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])

        idx = len(word1)
        while idx < len(word2):
            result.append(word2[idx])
            idx += 1
        return "".join(result)