class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        d=defaultdict(int)
        for i in range(10): d[i]=0
        for v in nums:
            t=[int(x) for x in str(v)]
            d[max(t)-min(t)]+=v

        for i in range(9, -1, -1):
            if d[i]: return d[i]