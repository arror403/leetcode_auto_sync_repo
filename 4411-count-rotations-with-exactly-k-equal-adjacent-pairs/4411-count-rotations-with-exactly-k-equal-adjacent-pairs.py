class Solution:
    def countRotations(self, s: str, k: int) -> int:
        L=len(s)
        s=s+s
        res=0

        for i in range(L):
            t=s[i:i+L]
            if sum(1 for j in range(L-1) if t[j]==t[j+1])==k: 
                res+=1


        return res