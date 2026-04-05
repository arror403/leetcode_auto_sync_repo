class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        d=defaultdict(int)
        for i in range(1, 1000):
            for j in range(i+1, 1000):
                t=(i**3+j**3)
                if t>n: break
                d[t]+=1

        return sorted([v for v,f in d.items() if f>1])