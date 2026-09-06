class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters_in_window = set([s[0]])
        longest_length = 1
        left = 0
        right = 1
        while (right < len(s)):
            if s[right] not in letters_in_window:
                longest_length = max(longest_length, right - left + 1)
                letters_in_window.add(s[right])
                right += 1
                
            else:
                #have to remove the duplicate letter
                while s[left] != s[right]:
                    letters_in_window.remove(s[left])
                    left += 1
                left += 1
                right += 1
        return longest_length
