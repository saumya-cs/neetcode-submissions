class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        if len(strs) == 0:
            return None
        for i in range(len(strs)):
            word += strs[i]
            if i != len(strs) - 1:
                word += " "
        print(word)
        return word

    def decode(self, s: str) -> List[str]:
        if s is None:
            return []
        if s == "":
            return [""]
        list = s.split()
        return list
