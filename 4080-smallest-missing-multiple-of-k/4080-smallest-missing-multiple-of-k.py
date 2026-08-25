class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s=set(nums)
        m=1

        while 1:
            if k*m not in s: return k*m
            m+=1