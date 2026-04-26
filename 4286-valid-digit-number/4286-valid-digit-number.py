class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        n,x=str(n),str(x)
        return n[0]!=x and x in n