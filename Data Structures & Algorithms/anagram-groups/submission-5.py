class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        returned = []
        alphabet_map = dict()
        for word in strs:
            key = "".join(sorted(word))
            lst = alphabet_map.get(key, [])
            lst.append(word)
            alphabet_map[key] = lst
        for _, lst in alphabet_map.items():
            returned.append(lst)
        return returned


        