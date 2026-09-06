class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        #edge cases: case insensitive (if an alphabet, lower both), if digit, compare digits, if non alphanumeric, skip it

        while(left < right):

            if(not s[left].isalnum()):
                left += 1
            if (not s[right].isalnum()):
                right -= 1
            
            if (left < right):
                if (s[left].isdigit() or s[right].isdigit()):
                    if (s[left] != s[right]):
                        return False
                else:
                    if (s[left].lower() != s[right].lower()):
                        return False
            
            left += 1
            right -= 1
        return True