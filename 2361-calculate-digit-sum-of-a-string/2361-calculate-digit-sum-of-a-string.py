class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            ns=[]
            for i in range(0, len(s), k):
                g=s[i:i+k]
                ds=sum(int(d) for d in g)
                ns.append(str(ds))
            s=''.join(ns)

        return s