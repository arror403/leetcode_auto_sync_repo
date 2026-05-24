class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        N = len(arr)
        # --- Step 1: Precompute Range Maximum Queries (RMQ) ---
        # max_in_range[i][j] stores the maximum value in arr[i...j]
        # O(N^2) setup time.
        max_in_range = [[0] * N for _ in range(N)]
        for i in range(N):
            max_in_range[i][i] = arr[i]
            for j in range(i + 1, N):
                max_in_range[i][j] = max(max_in_range[i][j-1], arr[j])

        def get_max_between(i: int, j: int) -> int:
            start = min(i, j) + 1
            end = max(i, j) - 1
            
            if start > end:
                return -1 # Empty range
            
            return max_in_range[start][end]

        def is_valid_jump(i: int, j: int) -> bool:
            if arr[i] <= arr[j]:
                return False

            max_k = get_max_between(i, j)
            
            return arr[i] > max_k

        dp = {}

        def dfs(i: int) -> int:
            if i in dp:
                return dp[i]

            max_len = 1
            
            for x in range(1, d + 1):
                
                j_right = i + x
                if j_right < N:
                    if is_valid_jump(i, j_right):
                        max_len = max(max_len, 1 + dfs(j_right))

                j_left = i - x
                if j_left >= 0:
                    if is_valid_jump(i, j_left):
                        max_len = max(max_len, 1 + dfs(j_left))
            
            dp[i] = max_len
            return max_len

        
        return max([dfs(i) for i in range(N)])