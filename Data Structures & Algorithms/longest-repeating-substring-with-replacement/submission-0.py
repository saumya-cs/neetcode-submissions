class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #find the most frequent character using dict
        char_frequencies = dict()
        numTimesMaxOccurred = 1
        most_frequent = s[0]
        for c in s:
            char_frequencies[c] = char_frequencies.get(c,0) + 1
            if (char_frequencies[c] > numTimesMaxOccurred):
                most_frequent = c
                numTimesMaxOccurred += 1

        # sliding window for replacements
        longest = 0
        left = 0
        right = 1
        kUsed = 0
        while (left < len(s)):
            longest = max(longest, right-left)
            if (right >= len(s)):
                return longest
            if (s[right] == most_frequent):
                right += 1
            elif (kUsed < k):
                kUsed += 1
                right += 1
            else:
                if (s[left] != most_frequent):
                    kUsed -= 1
                    left += 1
                else:
                    left = right
                    right = left + 1


        