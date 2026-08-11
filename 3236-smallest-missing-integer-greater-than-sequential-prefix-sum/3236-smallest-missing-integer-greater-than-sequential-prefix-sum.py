class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        L=len(nums)
        i=0
        res=nums[0]

        while i+1 < L and nums[i+1]==nums[i]+1:
            res+=nums[i+1]
            i+=1

        if res not in nums:
            return res
        else:
            while res in nums: res+=1
            return res     