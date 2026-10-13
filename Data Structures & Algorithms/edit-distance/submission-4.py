class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        editDistance[i][j] is min operations to turn first i chars of word1 into first j chars of word2

        editDistance[i][j] = min(insert, delete, replace)

        """
        editDistance = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
       
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0:
                    editDistance[i][j] = j
                elif j == 0:
                    editDistance[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    editDistance[i][j] = editDistance[i-1][j-1]
                else:
                    delete = editDistance[i-1][j] + 1
                    replace = editDistance[i-1][j-1] + 1
                    insert = editDistance[i][j-1] + 1
                    editDistance[i][j] = min(delete, replace, insert)
        return editDistance[-1][-1]

        