class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        d=[0]*len(nums)
        res=0
        for i in nums:
            c=0
            while d[i]==0:
                d[i]=1
                c+=1
                i=nums[i]
            res=max(res, c)

        return res 