class Solution:
    #longestPal[i][j] = True if substring from i to j is palindrome
    #so, if i == j, longestPal is True
    def longestPalindrome(self, s: str) -> str:
        longestPal = [[False] * len(s) for _ in range(len(s))] 
        resIdx, resLen = 0,0
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or longestPal[i+1][j-1] == True):
                    longestPal[i][j] = True
                    if (j - i + 1) > resLen:
                        resLen = j - i + 1
                        resIdx = i
        return s[resIdx : resIdx + resLen]

        

        