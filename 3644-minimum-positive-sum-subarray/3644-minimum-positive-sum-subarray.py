class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        P = [0]+list(accumulate(nums))
        return min(
            (
                P[j] - P[i]
                for i in range(len(nums))
                for j in range(i+l, min(len(P), i+r+1))
                if P[j] > P[i]
            ),
            default=-1,
        )