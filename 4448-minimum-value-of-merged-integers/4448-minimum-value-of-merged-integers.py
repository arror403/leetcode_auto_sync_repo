class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        nums=list(map(str, nums))
        return min(int(nums[i]+nums[i+1]) for i in range(0, len(nums), 2))