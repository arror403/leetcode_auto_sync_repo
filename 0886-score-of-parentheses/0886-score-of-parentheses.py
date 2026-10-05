class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res=d=0
        p='('

        for c in s:
            if c=='(': 
                d+=1
            else:
                d-=1
                if p=='(':
                    res+=1<<d
            p=c


        return res