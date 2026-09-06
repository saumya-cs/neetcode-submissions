class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        longest = 0
        my_set = set([s[left]])
        while (left < len(s)):
            longest = max(longest, right - left)
            if (s[right] not in my_set):
                my_set.add(s[right])
                right += 1
                if (right >= len(s)):
                    return longest
            else:
                my_set.remove(s[left])
                left += 1
                if (left == right):
                    left = right
                    right = left + 1
                    my_set = set([s[left]])
                    if (right >= len(s)):
                        return longest
        return longest
