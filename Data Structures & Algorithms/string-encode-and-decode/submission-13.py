class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        if len(strs) == 0:
            return "<EMPTY>"
        for i in range(len(strs)):
            word += str(len(strs[i]))
            word += "#"
            word += strs[i]
            #word += "#"
        return word

    def decode(self, s: str) -> List[str]:
        print(s)
        returned = []
        if s == "<EMPTY>":
            return returned
        if s[0] == 0:
            return [""]
        i = 0
        while i < len(s):
            number = ""
            while (s[i] != "#"):
                #reading the number
                number += s[i]
                print("hi")
                i+=1
            print(number)
            length = int(number)
            n = 0
            word = ""
            while (n < length):
                n+=1
                word += s[i + n]
                
            print("word = " + word)
            returned.append(word)
            i = i + n + 1

        return returned
