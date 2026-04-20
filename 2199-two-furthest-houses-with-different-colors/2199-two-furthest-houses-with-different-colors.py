class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        d=defaultdict(list)
        for i,v in enumerate(colors): d[v].append(i)

        res=0
        k=list(d.keys())
        for i in range(len(k)):
            for j in range(i+1, len(k)):
                res=max(res, d[k[j]][-1]-d[k[i]][0], d[k[i]][-1]-d[k[j]][0])


        return res