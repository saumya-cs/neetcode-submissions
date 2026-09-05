class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by = dict()
        trusts = set()
        for a,b in trust:
            adj_list = trusted_by.get(b, [])
            adj_list.append(a)
            trusted_by[b] = adj_list
            trusts.add(a)
        
        for node, adj_list in trusted_by.items():
            if len(adj_list) == n - 1:
                if node not in trusts:
                    return node
        return -1
        