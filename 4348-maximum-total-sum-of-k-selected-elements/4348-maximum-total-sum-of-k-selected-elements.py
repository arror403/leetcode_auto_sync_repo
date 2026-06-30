class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums=sorted(nums)[::-1]
        p=min(k, mul-1)
        res=j=0

        for _ in range(p):
            res+=nums[j]*mul
            mul-=1
            j+=1

        res+=sum(nums[j:j+k-p])


        return res