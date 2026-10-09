class Solution:
    def minInsertions(self, s: str) -> int:
        b=res=0
        for c in s:
            if c=='(':
                if b%2:
                    b-=1
                    res+=1
                b+=2
            else:
                b-=1
                if b<0:
                    b+=2
                    res+=1

        return res+b