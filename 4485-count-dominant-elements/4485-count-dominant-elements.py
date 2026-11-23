class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        res=0
        L=len(nums)
        if L==1: return 1
        for i in range(1, L-1):
            if nums[i]>=(nums[i-1]+nums[i+1])/2:
                res+=1

        if nums[0]>=nums[1]: res+=1
        if nums[-1]>=nums[-2]: res+=1

        return res