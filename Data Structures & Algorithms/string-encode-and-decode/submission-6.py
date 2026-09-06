class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for i in range(len(strs)):
            word += strs[i]
            if i != len(strs) - 1:
                word += " "
        return word

    def decode(self, s: str) -> List[str]:
        list = s.split()
        return list
