class Solution:
    def mirrorFrequency(self, s: str) -> int:
        d=Counter(s)
        seen=set()
        res=0
        for c in s:
            if c.isalpha():
                m=chr(219-ord(c))
            else:
                m=str(abs(9-int(c)))
            if (c,m) not in seen and (m,c) not in seen:
                res+=abs(d[c]-d[m])
                seen.add((c,m))
                seen.add((m,c))

        return res