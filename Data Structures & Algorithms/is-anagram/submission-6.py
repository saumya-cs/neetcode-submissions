class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charFreq = dict()
        if len(s) != len(t):
            return False
        for character in s:
            charFreq[character] = charFreq.get(character, 0) + 1
        for character in t:
            if character not in charFreq:
                return False
            if charFreq[character] == 0:
                return False
            charFreq[character] = charFreq[character] - 1
        
        for k,v in charFreq.items():
            if v > 0:
                return False
        return True
        