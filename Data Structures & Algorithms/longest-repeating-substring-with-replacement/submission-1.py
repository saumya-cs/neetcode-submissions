class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #always replace characters with the most frequent character in the string
        #num replacements = len(window) - freq(most freq char)
        #length of window = freq(most freq char) + k?
        left = 0
        max_freq = 0
        freq = dict()
        max_length = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0) + 1
            max_freq = max(max_freq, freq[s[right]])
            window_length = right - left + 1
            if (window_length - max_freq <= k):
                max_length = max(max_length, window_length)
            else:
                left += 1
        return max_length
        
        

