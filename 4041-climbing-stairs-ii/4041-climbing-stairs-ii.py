class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dp[j] = minimum cost to reach step j
        # Step 0 is our starting point (cost = 0)
        # Steps 1 to n have costs from the array
        # costs array is 1-indexed in the problem, so step j uses costs[j-1]
        
        dp=[inf]*(n+1)
        dp[0]=0

        for j in range(1, n+1):
            for i in [j-1, j-2, j-3]:
                if i<0: continue
                # Cost = cost to reach step i + cost of jumping to step j
                # costs[j-1] is the cost of step j (since costs is 0-indexed but 1-indexed in problem)
                jump_cost = costs[j-1] + (j-i)**2
                dp[j] = min(dp[j], dp[i] + jump_cost)
        
        return dp[n]