class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = set(s[0])
        maxLen = 1
        left = 0
        right = 1
        
        while right < len(s):
            if s[right] in seen: #start new window
                maxLen = max(right - left, maxLen)
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                left += 1
                right += 1
                
            else:
                seen.add(s[right])
                right += 1
        maxLen = max(right - left, maxLen)
        return maxLen

