class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        L=len(nums)
        dp=[[0]*L for _ in range(L)]

        def helper(s, e):
            if not dp[s][e]:
                dp[s][e] = nums[e] if s==e else max(nums[e]-helper(s,e-1), nums[s]-helper(s+1,e))
                # print(dp)
            return dp[s][e]


        return helper(0, L-1)>=0