class Solution:
    def longestValidParentheses(self, s: str) -> int:
        L=len(s)
        res=0
        t=[]

        for i in range(L):
            if s[i]=='(': 
                t.append(i)
            else:
                if t:
                    if s[t[-1]]=='(': 
                        t.pop()
                    else: 
                        t.append(i)
                else: 
                    t.append(i)

        if not t: 
            return L
        else:
            a,b=L,0
            while t:
                b=t.pop()
                res=max(res, a-b-1)
                a=b

            return max(res, a)