class Solution:
    def isValid(self, s: str) -> bool:
        d=[]
        p={')':'(', '}':'{', ']':'['}

        for c in s:
            if c in p:
                if d and d[-1]==p[c]:
                    d.pop()
                else:
                    return False
            else:
                d.append(c)


        return d==[] 