class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        M, m = max(nums), min(nums)
        t = [nums.index(M)+1, nums.index(m)+1, nums[::-1].index(M)+1, nums[::-1].index(m)+1]

        # print(M,m)
        # print(t)
        return min(max(t[0],t[1]), max(t[2],t[3]), t[0]+t[3], t[1]+t[2])