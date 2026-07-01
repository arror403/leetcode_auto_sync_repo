class Solution:
    def maxTargetNodes(self, e1: List[List[int]], e2: List[List[int]]) -> List[int]:
        
        def dfs(i, p, al, parity, even = True):
            targets = even
            parity[i] = even
            for j in al[i]:
                if (j != p):
                    targets += dfs(j, i, al, parity, not even)
            return targets

        def adjacencyList(edges):
            al = [[] for _ in range(len(edges) + 1)]
            for e in edges:
                al[e[0]].append(e[1])
                al[e[1]].append(e[0])            
            return al

        m, n = len(e1) + 1, len(e2) + 1
        parity = [False]*m 
        ingnored = [False]*n
        even1 = dfs(0, -1, adjacencyList(e1), parity)
        odd1 = m - even1
        even2 = dfs(0, -1, adjacencyList(e2), ingnored)
        odd2 = n - even2


        return [max(even2, odd2) + (even1 if parity[i] else odd1) for i in range(m)]