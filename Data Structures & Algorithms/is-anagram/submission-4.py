class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        sw1 = sorted(s)
        sw2 = sorted(t)

        for i in range(len(sw1)):
            if (sw1[i] != sw2[i]):
                return False
        return True