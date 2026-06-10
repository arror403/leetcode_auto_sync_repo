class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        res=0
        for x in range(k+n+1):
            if abs(n-x)<=k and n&x==0:
                res+=x

        return res