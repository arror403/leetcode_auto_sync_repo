class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        nums=[x%k for x in nums]
        res=0

        for r,g in groupby(nums):
            L=len(list(g))
            if ((L-1)*r)%k==0:
                res=max(res, L)
            else:
                d=k//gcd(r, k)
                res=max(res, ((L-1)//d)*d+1)


        return res