class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if set(nums)=={0}: return 0
        
        L=len(nums)
        t=reduce(operator.xor, nums)

        return L if t else L-1