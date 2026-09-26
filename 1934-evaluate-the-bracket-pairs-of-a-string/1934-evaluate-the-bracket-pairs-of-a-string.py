class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d={}
        for k,v in knowledge: d[k]=v

        t=0
        tmp=res=''
        for c in s:
            if c=='(':
                t=1
            elif c==')':
                res+=(d[tmp] if tmp in d.keys() else '?')
                t=0
                tmp=''
            else:
                if t: tmp+=c
                else: res+=c
            

        return res