class Solution:
    def processStr(self, s: str, k: int) -> str:
        Len=[0]*(10**5)
        L=0
        n=len(s)
        for i in range(n):
            c=s[i]
            if c=='*':
                L-=(1 if L>0 else 0)
            elif c=='#':
                L*=2
            else:
                L+=(1 if c!='%' else 0)

            Len[i]=L
            
        if (L-1)<k: return '.'
        
        for i in range(n-1, -1, -1):
            c=s[i]
            L=Len[i]
            if L==0: continue
            
            if c=='*':
                continue
            elif c=='#':
                if k>=L//2: k-=L//2
            elif c=='%':
                k=L-1-k
            else:
                if k==L-1: return c
        
        return '.'