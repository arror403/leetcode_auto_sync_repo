class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        L = len(nums) >> 1
        nums = sorted([x*x for x in nums])

        return sum(nums[L:]) - sum(nums[:L])