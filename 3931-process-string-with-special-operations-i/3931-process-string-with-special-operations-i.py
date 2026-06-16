class Solution:
    def processStr(self, s: str) -> str:
        p={'*','#','%'}
        res=[]
        for c in s:
            if c not in p:
                res.append(c)
            elif c=='*':
                if res: res.pop()
            elif c=='#':
                res*=2
            else:
                res=res[::-1]

        return ''.join(res) if res else ""