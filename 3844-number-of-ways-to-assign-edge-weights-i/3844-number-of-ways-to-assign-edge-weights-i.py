class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        def dfs(adj, cur, parent):
            depth = 0
            for node in adj[cur]:
                if node == parent: continue
                depth = max(depth, dfs(adj, node, cur) + 1)

            return depth

        MOD = 10**9 + 7
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
            
        depth = dfs(adj, 1, 0) - 1
        res = 1

        while depth:
            res = (res*2)%MOD
            depth -= 1


        return res