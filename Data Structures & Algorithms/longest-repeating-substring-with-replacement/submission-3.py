from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        window_dict = defaultdict(int)
        right = 0
        longest = 0
        while right < len(s):
            window_dict[s[right]] += 1
            sorted_list = sorted(window_dict.values())
            while left < len(s) and sum(sorted_list) - sorted_list[-1] > k:
                
                window_dict[s[left]] -= 1
                left += 1
            longest = max(right - left + 1,longest)
            right += 1
            
        return longest