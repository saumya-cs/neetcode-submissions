class Solution:
    def countSubstrings(self, s: str) -> int:
        palCount = 0
        for center in range(len(s)):
            #odd palindromes
            index = 0
            while (center + index < len(s)) and (center - index >= 0) and s[center + index] == s[center - index]:
                palCount += 1
                index += 1
            
            index1 = 0 
            index2 = 1
            while (center - index1 >= 0) and (center + index2 < len(s)) and (s[center -index1] == s[center + index2]):
                palCount += 1
                index1 += 1
                index2 += 1
        return palCount