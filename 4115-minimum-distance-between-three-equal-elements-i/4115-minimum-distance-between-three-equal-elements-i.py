class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return -1
        
        d = defaultdict(list)
        for i in range(n): d[nums[i]].append(i)

        res = inf
        for t in d.values():
            L = len(t)
            if L < 3: continue
            for i in range(L - 2):
                res = min(res, (t[i+2] - t[i]))
        # i < j < k
        # (k-i)*2
        return -1 if res == inf else res * 2