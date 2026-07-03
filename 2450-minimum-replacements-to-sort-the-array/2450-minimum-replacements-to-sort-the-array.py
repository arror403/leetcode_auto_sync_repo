class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        t=nums[-1]
        res=0
        for n in nums[::-1]:
            k=(n+t-1)//t
            t=n//k
            res+=(k-1)

        return res