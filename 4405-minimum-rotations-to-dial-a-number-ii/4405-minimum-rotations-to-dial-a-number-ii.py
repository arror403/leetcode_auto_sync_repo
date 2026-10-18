class Solution:
    def minRotations(self, n: int, s: str) -> int:
        def dist(x,y):
            x,y=int(x),int(y)
            d=(x-y if x>y else y-x)
            return min(d, 10-d)

        p=Counter(pairwise('0'+s))
        res=sum(dist(v[0],v[1])*f for v,f in p.items())
        g=max(dist(a,b)-dist(a,s[-1]) for a,b in p)

        return res-g