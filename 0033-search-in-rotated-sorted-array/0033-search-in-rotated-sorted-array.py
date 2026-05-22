class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L=len(nums)
        l,r=0,L-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid

        ro=l
        l,r=0,L-1
        while l<=r:
            mid=(l+r)//2
            r_mid=(mid+ro)%L
            if nums[r_mid]==target:
                return r_mid
            if nums[r_mid]<target:
                l=mid+1
            else:
                r=mid-1


        return -1