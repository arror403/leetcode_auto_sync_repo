class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        res=inf
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==3:
                    res=min(res,(j-i))

        return res if res!=inf else -1