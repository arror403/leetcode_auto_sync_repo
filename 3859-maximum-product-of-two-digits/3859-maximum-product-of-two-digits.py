class Solution:
    def maxProduct(self, n: int) -> int:
        return max(int(a)*int(b) for a,b in combinations(str(n),2))