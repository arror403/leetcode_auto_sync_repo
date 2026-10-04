class Solution:
    def minRotations(self, s: str) -> int:
        s=[0]+list(map(int,s))
        res=0

        for i in range(1, len(s)):
            d=abs(s[i]-s[i-1])
            res+=min(d, abs(10-d))


        return res