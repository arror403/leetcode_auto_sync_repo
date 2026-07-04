class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        L=len(nums)
        c=[1]+[0]*(2*L+2)
        a=c[:]
        res=pre=0

        for v in nums:
            pre+=(1 if v==target else -1)
            c[pre]+=1
            a[pre]=a[pre-1]+c[pre]
            res+=a[pre-1]


        return res