class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res=0
        l=0
        c=defaultdict(int)
        
        for i,v in enumerate(nums):
            c[v]+=1
            while c[v]==(k+1):
                c[nums[l]]-=1
                l+=1

            res=max(res, i-l+1)


        return res