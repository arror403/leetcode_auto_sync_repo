class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        a0 = nums.count(0)
        t = nums[::-1][:a0]

        return a0 - t.count(0)