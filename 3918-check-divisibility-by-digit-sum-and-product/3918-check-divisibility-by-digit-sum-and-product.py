class Solution:
    def checkDivisibility(self, n: int) -> bool:
        d=list(map(int,str(n)))

        return n%(sum(d)+prod(d))==0