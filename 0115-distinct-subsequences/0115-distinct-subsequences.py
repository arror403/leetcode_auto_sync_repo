class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ls, lt = len(s), len(t)
        dp=[[0]*(ls+1) for _ in range(lt+1)]

        for c in range(ls): dp[0][c]=1

        for x in range(1, ls+1):
            for y in range(1, lt+1):
                if s[x-1]==t[y-1]:
                    dp[y][x]=dp[y-1][x-1]+dp[y][x-1]
                else:
                    dp[y][x]=dp[y][x-1]


        return dp[-1][-1]