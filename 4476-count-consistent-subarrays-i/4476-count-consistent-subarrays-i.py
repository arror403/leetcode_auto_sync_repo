class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        subs=[nums[p:q+1] for p in range(len(nums)) for q in range(p, len(nums))]
        return sum(1 if reduce(operator.and_, a)==min(a) else 0 for a in subs)