class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        c, m = comb(n-1, k-1), (10**9 + 7)
        return c%m if (n-k)%2 else (c-comb((n+k)//2-1, k-1))%m

        #return c #if (n+k)%2 else (c>>1)%m