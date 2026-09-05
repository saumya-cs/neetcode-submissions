class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        longest = 0
        if(left >= len(s)):
            return longest
        my_set = set([s[left]])
        while (left < len(s)):
            longest = max(longest, right - left)
            if (right >= len(s)):
                    return longest
            
            if (s[right] not in my_set):
                my_set.add(s[right])
                right += 1
                
            else:
                my_set.remove(s[left])
                left += 1
                if (left == right):
                    left = right
                    right = left + 1
                    if(left >= len(s)):
                        return longest
                    my_set = set([s[left]])
                
        return longest
