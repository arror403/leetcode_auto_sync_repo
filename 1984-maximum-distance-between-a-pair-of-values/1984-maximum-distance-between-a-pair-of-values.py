class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res=j=0
        lj=len(nums2)

        for i,v in enumerate(nums1):
            while j<lj and nums2[j]>=v:
                j+=1

            res=max(res, j-i-1)


        return res