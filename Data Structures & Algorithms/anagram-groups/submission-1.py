class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #let's use sorted strings as keys with the actual words as values. 
        #keep track of sorted strings in a set and can be used to create output lists
        myMap = dict()
        output = []
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            if (key in myMap):
                myMap[key].append(strs[i])
            else:
                myMap[key] = [strs[i]]
        for key in myMap.keys():
            output.append(myMap[key])
        return output

        