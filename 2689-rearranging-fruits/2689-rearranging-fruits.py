class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        d1,d2=Counter(basket1),Counter(basket2)
        k=set(d1.keys())|set(d2.keys())
        diff=defaultdict(int)

        for x in k:
            if (d1[x]+d2[x])%2:
                return -1
            elif d1[x]==d2[x]:
                continue
            else:
                diff[x]=(d1[x]-d2[x])>>1

        l=[]
        for x,v in diff.items():
            l+=[x]*abs(v)
        l.sort()

        mn=min(min(basket1),min(basket2))

        return sum(min(x,2*mn) for x in l[:len(l)//2])