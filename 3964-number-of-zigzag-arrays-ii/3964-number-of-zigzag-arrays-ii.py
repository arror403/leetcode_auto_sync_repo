import numpy as np

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        M=10**9+7
        k=r-l+1
        m=np.array([[int(i+j+1 < k) for j in range(k)] for i in range(k)], dtype=object)
        res=np.array([1]*k, dtype=object)
        n-=1
        while n:
            if n&1: res=(res@m)%M
            m=(m@m)%M
            n>>=1
        
        return int(res.sum()*2%M)