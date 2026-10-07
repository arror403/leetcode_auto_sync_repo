class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isvalid(s):
            cnt=0
            for c in s:
                if c=='(':
                    cnt+=1
                elif c==')':
                    cnt-=1
                    if cnt<0: return False
            return cnt==0

        level={s}
        while 1:
            valid=[]
            for e in level:
                if isvalid(e): 
                    valid.append(e)

            if valid: return valid

            level=set(e[:i]+e[i+1:] for e in level for i in range(len(e)))