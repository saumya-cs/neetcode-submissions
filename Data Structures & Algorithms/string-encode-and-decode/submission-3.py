class Solution:

    def encode(self, strs: List[str]) -> str:
        output = str()
        for i in range(len(strs)):
            output += strs[i]
            if (i < len(strs) - 1):
                output += " "
        return output
    def decode(self, s: str) -> List[str]:
        if (len(s) == 0):
            return [""]
        list = s.split(" ")
        return list
