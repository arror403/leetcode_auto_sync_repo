class Solution:
    def maxProduct(self, n: int) -> int:
        d=sorted(list(map(int,str(n))))
        return d[-1]*d[-2]