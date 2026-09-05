class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapToAlphabetical = dict()

        for word in strs:
            key = "".join(sorted(word))
            curr = (mapToAlphabetical.get(key, []))
            if (curr is None):
                curr = [word]
            else:
                curr.append(word)
            mapToAlphabetical[key] = curr
        returned = []
        for key,val in mapToAlphabetical.items():
            returned.append(val)
        
        return returned
        