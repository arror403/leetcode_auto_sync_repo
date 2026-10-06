class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l=r=0

        for c in s:
            if r==0 and c==')':
                l+=1
            else:
                r+=(1 if c=='(' else -1)


        return l+r