from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #fixed window of size len(s1)
        s1_freq = defaultdict(int)
        for c in s1:
            s1_freq[c] += 1
        
        curr_map = s1_freq.copy()
        left,right = 0,0
        while right < len(s2):
            
            curr_map[s2[right]] -= 1
            
            right += 1
            
            if (right - left == len(s1)):
                allTrue = True
                for val in curr_map.values():
                    if val != 0: allTrue = False
                if allTrue: return True
                curr_map[s2[left]] += 1
                left += 1
            
                
            
        return False