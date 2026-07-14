class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod = 10**9 + 7 
        M = max(nums)
        dp = [[0]*(M+1) for _ in range(M+1)]
        dp[0][0] = 1

        for a in nums:
            dp2 = [[0]*(M+1) for _ in range(M+1)]
            for i in range(M, -1, -1):
                for j in range(M, -1, -1):
                    v = dp[i][j]
                    i2 = gcd(i, a)
                    j2 = gcd(j, a)
                    dp2[i2][j] = (dp2[i2][j] + v) % mod
                    dp2[i][j2] = (dp2[i][j2] + v) % mod
                    dp2[i][j] = (dp2[i][j] + v) % mod

            dp = dp2

        res = 0
        for i in range(1, M+1): res = (res + dp[i][i]) % mod

        return res