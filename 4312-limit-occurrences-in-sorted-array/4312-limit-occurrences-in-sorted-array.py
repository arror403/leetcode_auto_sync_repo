class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res=[]
        for l,g in groupby(nums):
            g=list(g)
            if len(g)>=k:
                res+=[l]*k
            else:
                res+=g

        return res