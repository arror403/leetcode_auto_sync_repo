class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        # gemma-4-26B-A4B-it-UD-Q4_K_M.gguf
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Precompute subtree XORs and discovery/finish times
        subtree_xor = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        # Using iterative DFS to avoid recursion depth issues and for speed
        # stack stores (node, parent, index_in_adj_list)
        stack = [(0, -1)]
        order = []
        
        # First pass: build discovery order and parent relations
        visited_order = []
        parent = [-1] * n
        stack = [0]
        visited = [False] * n
        visited[0] = True
        
        # Standard DFS to get traversal order for post-order processing
        stack = [0]
        order = []
        parent = [-1] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0
        
        # To handle tin/tout and subtree XOR, we'll use a standard recursive-style approach
        # but implemented carefully.
        sys.setrecursionlimit(2000)
        
        def dfs(u, p):
            nonlocal timer
            timer += 1
            tin[u] = timer
            res = nums[u]
            for v in adj[u]:
                if v != p:
                    res ^= dfs(v, u)
            subtree_xor[u] = res
            tout[u] = timer
            return res

        total_xor = dfs(0, -1)

        # Helper to check if u is ancestor of v
        def is_ancestor(u, v):
            return tin[u] <= tin[v] and tout[u] >= tout[v]

        # We iterate through all pairs of nodes (excluding root 0)
        # Each node i > 0 represents the edge between i and its parent.
        ans = float('inf')
        
        # Pre-collect all nodes except root to iterate efficiently
        nodes = list(range(1, n))
        
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                u, v = nodes[i], nodes[j]
                
                if is_ancestor(u, v):
                    # v is in u's subtree
                    x1 = subtree_xor[v]
                    x2 = subtree_xor[u] ^ subtree_xor[v]
                    x3 = total_xor ^ subtree_xor[u]
                elif is_ancestor(v, u):
                    # u is in v's subtree
                    x1 = subtree_xor[u]
                    x2 = subtree_xor[v] ^ subtree_xor[u]
                    x3 = total_xor ^ subtree_xor[v]
                else:
                    # Subtrees are disjoint
                    x1 = subtree_xor[u]
                    x2 = subtree_xor[v]
                    x3 = total_xor ^ subtree_xor[u] ^ subtree_xor[v]
                
                score = max(x1, x2, x3) - min(x1, x2, x3)
                if score < ans:
                    ans = score
                    if ans == 0: return 0 # Optimization: can't get better than 0
                    
        return ans