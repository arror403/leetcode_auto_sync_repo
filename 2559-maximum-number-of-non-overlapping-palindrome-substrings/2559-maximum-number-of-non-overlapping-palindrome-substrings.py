class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        res=start=0 
        L=len(s)

        for c in range(L*2-1):
            l=c>>1
            r=l+c%2
            while l>=start and r<L and s[l]==s[r]:
                if (r+1-l)>=k: 
                    res+=1
                    start=r+1
                    break
                l-=1
                r+=1


        return res