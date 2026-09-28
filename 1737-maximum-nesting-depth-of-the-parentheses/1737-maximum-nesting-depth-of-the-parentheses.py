class Solution:
    def maxDepth(self, s: str) -> int:
        res=t=0

        for c in s:
            if c=='(':
                t+=1
            elif c==')':
                t-=1

            res=max(t, res)
        

        return res