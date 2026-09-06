class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in range(len(strs)):
            output += strs[i]
            if (i < len(strs) - 1):
                output += " "
        return output
    def decode(self, s: str) -> List[str]:
        list = s.split(" ")
        return list
