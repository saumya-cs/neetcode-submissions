class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #iterate over second string
        # if the first string contains that character, edit it 
        # with concatenation so that it removes that letter
        bank = s
        for char in t: 
            index = bank.find(char)
            if index == -1: 
                return False
            else: 
                bank = bank[0:index] + bank[index:]
        return True   
