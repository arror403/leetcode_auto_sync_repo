class Solution:
    def findMin(self, nums: List[int]) -> int:
        # t=nums+nums
        # [4,5,6,7, 0,1,2,4,5,6,7, 0,1,2]
        
        return nums[bisect_left(nums, True, key=lambda x: x<=nums[-1])]