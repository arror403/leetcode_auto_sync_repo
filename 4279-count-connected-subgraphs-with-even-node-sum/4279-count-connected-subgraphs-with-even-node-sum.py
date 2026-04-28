class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        
        # 1. Build the adjacency structure (Adjacency List is usually faster than matrix)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def is_connected(subset: tuple[int]) -> bool:
            
            # Checks if connected
            if not subset:
                return False
            
            # Start BFS from the first node in the subset
            start_node = subset[0]
            
            queue = deque([start_node])
            visited = {start_node}
            
            # Set for quick membership check of nodes in the induced subgraph
            subset_set = set(subset)

            while queue:
                u = queue.popleft()
                
                # Check all neighbors of u
                for v in adj[u]:
                    # Condition 1: The neighbor v must be part of the subset 't'
                    # Condition 2: v must not have been visited yet
                    if v in subset_set and v not in visited:
                        visited.add(v)
                        queue.append(v)
            
            # If the number of visited nodes equals the size of the subset, it is connected.
            return len(visited) == len(subset)

        count = 0
        
        # Iterate through all possible subset sizes, r, from 1 to N
        for r in range(1, n + 1):
            # Iterate through all combinations (subsets) of size r
            for subset_tuple in combinations(range(n), r):
                
                # 2. Check the Sum Condition (Parity)
                current_sum = sum(nums[i] for i in subset_tuple)
                if current_sum % 2 != 0:
                    continue  # Skip if the sum is odd

                # 3. Check the Connectivity Condition
                if is_connected(subset_tuple):
                    count += 1
                    
        return count