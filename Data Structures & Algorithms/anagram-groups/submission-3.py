class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = [] # array of arrays of strings string**
        anagramByAlphaOrder = dict()

        for word in strs:
            alphaWordKey = "".join(sorted(word))

            currList = anagramByAlphaOrder.get(alphaWordKey, [])
            currList.append(word)
            anagramByAlphaOrder[alphaWordKey] = currList
        
        for key,value in anagramByAlphaOrder.items():
            anagrams.append(value)
        
        return anagrams


        