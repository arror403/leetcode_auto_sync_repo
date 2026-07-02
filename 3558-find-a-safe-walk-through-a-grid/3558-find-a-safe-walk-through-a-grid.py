class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        # Min-heap stores (cost, r, c)
        pq = [(grid[0][0], 0, 0)]
        # dist[r][c] stores the minimum cost to reach (r, c)
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]

        while pq:
            d, r, c = heapq.heappop(pq)
            if d > dist[r][c]:
                continue
            if r == m - 1 and c == n - 1:
                return d < health
            
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_dist = d + grid[nr][nc]
                    if new_dist < dist[nr][nc] and new_dist < health:
                        dist[nr][nc] = new_dist
                        heapq.heappush(pq, (new_dist, nr, nc))
                        

        return False