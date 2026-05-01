class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        L=len(nums)
        S=sum(nums)

        res=sum(i*x for i,x in enumerate(nums))
        t=res

        for i in range(1, L):
            t+=S-L*nums[L-i]
            res=max(res, t)


        return res