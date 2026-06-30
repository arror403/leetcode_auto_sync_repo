class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        d = {'a':0, 'b':0, 'c':0}
        j = 0
        for i, c in enumerate(s):
            d[c] += 1
            while all(d.values()):
                d[s[j]] -= 1
                j += 1
            res += j

        return res