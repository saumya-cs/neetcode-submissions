class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        longestCommon[i][j] = longest subsequence that exists within first i chars of text1 and first j chars of text2

        longestCommon[i][j] = 
        """
        longestCommon = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    longestCommon[i][j] = longestCommon[i-1][j-1] + 1
                else:
                     longestCommon[i][j] = max(longestCommon[i-1][j], longestCommon[i][j-1])
        return longestCommon[-1][-1]

        