class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        right = 1
        longest = 0
        if not s:
            return 0
        seen.add(s[left])
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            right += 1
            longest = max(longest, right - left)
        return longest
                
        