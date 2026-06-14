class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        d=list(map(int,str(n)))
        return (sum(x**2 for x in d)-sum(d)) >= 50