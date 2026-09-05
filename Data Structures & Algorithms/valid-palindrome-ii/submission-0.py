class Solution:
    def validPalindrome(self, s: str) -> bool:

        def helper(left, right, deleted):
            if left > right:
                return True
            if s[left] != s[right]:
                if deleted:
                    return False
                else:
                    return helper(left + 1, right, True) or helper(left, right-1, True)
            return helper(left + 1, right - 1, deleted)
        return helper(0, len(s) - 1, False)