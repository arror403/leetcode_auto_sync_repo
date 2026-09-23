class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        res = inf
        current_sum = l = 0
        L = len(nums)

        for r in range(L):
            current_sum += nums[r]
            
            while current_sum > target and l <= r:
                current_sum -= nums[l]
                l+=1
                
            if current_sum == target:
                res = min(res, L-(r-l+1))


        return res if res != inf else -1