class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        if not grid or not grid[0]:
            return False
        
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c, prev_r, prev_c, char):
            # Mark the current cell as visited
            visited.add((r, c))
            # Standard 4-directional movement: down, up, right, left
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # 1. Check bounds
                # 2. Check if the neighbor has the same character
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == char:
                    # If the neighbor is already visited and it's NOT the parent, 
                    # we found a cycle!
                    if (nr, nc) in visited:
                        if (nr, nc) != (prev_r, prev_c):
                            return True
                    else:
                        # If not visited, recurse
                        if dfs(nr, nc, r, c, char):
                            return True
            
            return False

        # Iterate through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell hasn't been visited, start a DFS from here
                if (r, c) not in visited:
                    # We pass -1, -1 as the initial parent coordinates
                    if dfs(r, c, -1, -1, grid[r][c]):
                        return True
                        
                        
        return False