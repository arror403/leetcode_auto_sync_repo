class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        t=-inf
        res=[-1,-1]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and (nums[i]+nums[j])==target and nums[i]>nums[j]:
                    p=nums[i]*nums[j]
                    if p>t:
                        t=p
                        res=[i,j]


        return res