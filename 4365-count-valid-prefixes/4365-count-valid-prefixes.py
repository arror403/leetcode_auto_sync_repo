class Solution:
    def countValidPrefixes(self, s: str) -> int:
        n0=n1=res=0
        for c in s:
            if c=='1':  n1+=1
            else:       n0+=1

            if abs(n0-n1)<=1: res+=1

        return res