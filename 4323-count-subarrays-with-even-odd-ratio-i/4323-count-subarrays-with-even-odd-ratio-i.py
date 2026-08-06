class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        L=len(nums)
        res=0

        for i in range(L):
            x=y=0
            for j in range(i, L):
                if nums[j]&1: y+=1
                else: x+=1

                res+=int(b*x<=a*y)


        return res