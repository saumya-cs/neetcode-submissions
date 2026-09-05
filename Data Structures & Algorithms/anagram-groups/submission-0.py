class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # use sets for letters?
        returned = []
        added = False
        #iterate through the original list of strings
        for index in range(len(strs)): 
            #iterate through bases
            for i in range(len(returned)): 
                one = sorted(returned[i][0])
                two = sorted(strs[index])

                if (one == two): 
                    #add to mini list within returned
                    returned[i].append(strs[index])
                    added = True
            if not added:
                returned.append([strs[index]])
            added = False;
                    
        return returned
                

