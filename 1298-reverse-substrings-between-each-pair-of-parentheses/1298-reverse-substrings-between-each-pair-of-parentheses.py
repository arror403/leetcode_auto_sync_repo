class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        t=list(s)
        
        for i,c in enumerate(t):
            if c=='(':
                stack.append(i)
            elif c==')':
                j=stack.pop()
                t[j:i]=t[i:j:-1]  # Reverse the substring between j and i
        
        
        return ''.join([x for x in t if x not in '()'])