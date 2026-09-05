class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string))
            encoded += "#"
            encoded += string
        return encoded
    def decode(self, s: str) -> List[str]:
        strs = []
        number = ""
        i = 0
        while i < len(s):
            c = s[i]
            while c != '#':
                number += c
                i += 1
                c = s[i]
            i += 1
            length = int(number)
            number = ""
            string = ""
            for k in range(length):
                c = s[i]
                string += c
                i += 1
            strs.append(string)
        return strs