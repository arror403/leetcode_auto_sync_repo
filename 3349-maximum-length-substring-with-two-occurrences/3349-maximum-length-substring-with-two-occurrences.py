class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res=0
        t=[s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]

        for x in t:
            if all([v<=2 for v in Counter(x).values()]):
                res=max(res, len(x))


        return res