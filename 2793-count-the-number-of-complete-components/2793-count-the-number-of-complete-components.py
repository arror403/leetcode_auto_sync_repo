class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        res = 0
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, component):
            visited[node] = True
            component.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component)
        
        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i, component)
                
                is_complete = True
                size = len(component)
  
                for node in component:
                    if len(adj[node]) != size - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    res += 1
        
        
        return res