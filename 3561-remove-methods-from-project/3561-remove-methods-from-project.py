class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        
        # test using Ollama, open-webui and gguf (Qwen3.6) in Docker


        # Step 1: Build adjacency list for the directed graph
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
            
        # Step 2: Find all suspicious methods (reachable from k) using iterative DFS/BFS
        suspicious = [False] * n
        stack = [k]
        suspicious[k] = True
        
        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                if not suspicious[neighbor]:
                    suspicious[neighbor] = True
                    stack.append(neighbor)
                    
        # Step 3: Check the removal condition
        # "No method outside the group invokes any methods within it"
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))  # Condition fails, remove nothing
                
        # Step 4: Return all remaining (non-suspicious) methods
        return [i for i in range(n) if not suspicious[i]]