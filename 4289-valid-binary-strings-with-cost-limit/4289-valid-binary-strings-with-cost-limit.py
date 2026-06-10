class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        res=[]
    
        def bt(s, k, n):
            if n==0:
                if k>=0:
                    res.append(s)
                return
            
            L=len(s)
            if(L==0 or s[L-1]!='1'): bt(s+'1', k-L, n-1)
            
            bt(s+'0', k, n-1)


        bt('', k, n)
        
        return res