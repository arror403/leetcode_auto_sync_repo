class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d=defaultdict(list)
        for i, v in enumerate(nums): d[v].append(i)

        res=inf
        for t in d.values():
            if len(t)<3: continue
            for i in range(0, len(t)-2):
                res=min(res, t[i+2]-t[i])


        return -1 if res==inf else res*2