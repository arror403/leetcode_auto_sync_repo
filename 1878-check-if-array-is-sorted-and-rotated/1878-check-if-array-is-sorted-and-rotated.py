class Solution:
    def check(self, nums: List[int]) -> bool:
        s=sorted(nums)

        for i in nums:
            if nums==s:
                return True
            else:
                nums=nums[1:]+nums[:1]
            
            
        return False