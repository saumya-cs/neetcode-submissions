class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = dict()
        for i in range(len(order)):
            orderMap[order[i]] = i
        for w in range(1, len(words)):
            word1 = words[w - 1]
            word2 = words[w]
            isSame = True
            for i in range(min(len(word1), len(word2))):
                if orderMap[word1[i]] > orderMap[word2[i]]:
                    return False
                if orderMap[word1[i]] < orderMap[word2[i]]:
                    isSame = False
                    break
                    
            if isSame and (len(word1) > len(word2)):
                return False
        return True
            

        