class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        d={}
        res=inf
        for i in range(len(nums)):
            if nums[i] in d: res=min(res, i-d[nums[i]])
            d[int(str(nums[i])[::-1])]=i

        return res if res!=inf else -1