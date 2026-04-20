class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        # llama-b8854-bin-win-vulkan-x64 
        # gemma-4-E4B-it-UD-Q5_K_XL.gguf

        # Initialize the grid (final_grid) and distance tracking (dist)
        # final_grid stores the resulting color (0 means uncolored initially)
        final_grid = [[0] * m for _ in range(n)]
        
        # dist stores the minimum time required for a color to reach (r, c)
        # Initialize to infinity
        dist = [[math.inf] * m for _ in range(n)]
        
        # Priority Queue: stores tuples of (time, -color, r, c)
        # We use -color because heapq is a min-heap, and we want the LARGEST color
        # to have the highest priority when times are equal.
        pq = []
        
        # 1. Initialize sources
        for r, c, color in sources:
            if final_grid[r][c] == 0: # Handle potential overlapping sources (though unlikely based on problem constraints)
                final_grid[r][c] = color
                dist[r][c] = 0
                # Push (time, -color, r, c)
                heapq.heappush(pq, (0, -color, r, c))

        # Directions for adjacent cells (Up, Down, Left, Right)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 2. Dijkstra/BFS Propagation
        while pq:
            t, neg_c, r, c = heapq.heappop(pq)
            current_color = -neg_c

            # Stale entry check: If we found a faster or equal-time path already processed, skip.
            # We must also check the color, because if the current color is less than the recorded color, 
            # this state is obsolete.
            if t > dist[r][c] or current_color < final_grid[r][c]:
                continue
            
            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Boundary check
                if 0 <= nr < n and 0 <= nc < m:
                    t_new = t + 1
                    c_new = current_color
                    
                    # Retrieve the current state of the neighbor
                    c_old = final_grid[nr][nc]
                    d_old = dist[nr][nc]

                    # Case 1: Found a strictly faster path
                    if t_new < d_old:
                        dist[nr][nc] = t_new
                        final_grid[nr][nc] = c_new
                        heapq.heappush(pq, (t_new, -c_new, nr, nc))
                    
                    # Case 2: Arrived at the same time
                    elif t_new == d_old:
                        # Tie-breaker rule: Max color wins
                        if c_new > c_old:
                            # New color wins the tie
                            final_grid[nr][nc] = c_new
                            # Since the color changed, we must push this state back 
                            # to propagate the superior color further.
                            heapq.heappush(pq, (t_new, -c_new, nr, nc))
                    
                    # Case 3: Arrived slower (t_new > d_old)
                    # Do nothing, the current state is better or equal.

        return final_grid

# # Example Usage
# if __name__ == '__main__':
#     solver = Solution()
    
#     # Example 1
#     n1 = 3
#     m1 = 3
#     sources1 = [[0, 0, 1], [2, 2, 2]]
#     output1 = solver.solve_coloring(n1, m1, sources1)
#     print("Example 1 Output:")
#     for row in output1:
#         print(row)
#     # Expected: [[1, 1, 2], [1, 2, 2], [2, 2, 2]]

#     print("-" * 20)

#     # Example 2: Testing color dominance at same time
#     # 2x2 grid. Source A (0,0,1) and Source B (1,1,5).
#     # (0, 1) and (1, 0) both take 1 step. 5 > 1, so 5 wins.
#     n2 = 2
#     m2 = 2
#     sources2 = [[0, 0, 1], [1, 1, 5]]
#     output2 = solver.solve_coloring(n2, m2, sources2)
#     print("Example 2 Output:")
#     for row in output2:
#         print(row)
#     # Expected: [[1, 5], [5, 5]] 
