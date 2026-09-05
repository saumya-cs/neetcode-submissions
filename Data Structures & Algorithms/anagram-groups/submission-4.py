class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = dict()
        for word in strs:
            key = ''.join(sorted(word))
            lst = anagram_map.get(key, [])
            lst.append(word)
            anagram_map[key] = lst
        return list(anagram_map.values())
        