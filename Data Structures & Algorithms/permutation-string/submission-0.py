class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #fixed window problem
        left = 0
        right = len(s1) - 1
        target = sorted(s1)
        while (right < len(s2)):
            potential = sorted(s2[left:right+1])
            if (target == potential):
                return True
            left += 1
            right += 1
        return False

        