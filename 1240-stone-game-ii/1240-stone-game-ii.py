class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        L=len(piles)
        p=list(accumulate(piles[::-1]))[::-1]

        @lru_cache(maxsize=None)
        def dp(i, m):
            if (i + 2*m) >= L: return p[i]
            return p[i] - min(dp(i+x, max(m, x)) for x in range(1, 2*m + 1))


        return dp(0, 1)