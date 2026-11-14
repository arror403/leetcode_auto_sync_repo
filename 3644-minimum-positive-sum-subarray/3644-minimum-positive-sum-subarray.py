class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        L=len(nums)
        res=inf
        found=False

        for start in range(L):
            s=0
            for end in range(start,L):
                s += nums[end]
                length = end-start+1
                if (length>=l and length<=r and s>0):
                    res = min(res, s)
                    found=True


        return res if found else -1