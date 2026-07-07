class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=''
        s=0
        for v in str(n):
            if v!='0': x+=v
            s+=int(v)

        return s*int(x) if x else 0