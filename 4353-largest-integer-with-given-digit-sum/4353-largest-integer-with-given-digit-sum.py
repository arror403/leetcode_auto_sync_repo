class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s>n*9: return -1

        res=''
        p,q=divmod(s,9)
        while s and n:
            n-=1
            if p:
                res+='9'
                s-=9
                p-=1
            else:
                res+=str(q)
                break

        if n: res+='0'*n


        return int(res)