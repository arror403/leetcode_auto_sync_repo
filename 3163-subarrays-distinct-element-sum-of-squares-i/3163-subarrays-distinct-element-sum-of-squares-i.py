class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res=0
        L=len(nums)
        
        for i in range(L):
            s=set()
            for j in range(i, L):
                if nums[j] not in s: s.add(nums[j])
                res+=len(s)*len(s)
        

        return res