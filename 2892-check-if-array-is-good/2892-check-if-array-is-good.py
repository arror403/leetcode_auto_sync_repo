class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m=max(nums)
        return Counter(list(range(1,m+1))+[m])==Counter(nums)