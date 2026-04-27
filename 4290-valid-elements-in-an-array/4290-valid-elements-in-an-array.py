class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        L=len(nums)
        if L==1: return nums

        res=[nums[0]]
        for i in range(1,L-1):
            if nums[i]>max(nums[:i]) or nums[i]>max(nums[i+1:]):
                res.append(nums[i])

        res.append(nums[-1])

        return res