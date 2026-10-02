class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(curr, l, r):
            if len(curr)==n*2:
                res.append(curr)
                return
            
            if l<n: backtrack(curr+'(', l+1, r)
            
            if r<l: backtrack(curr+')', l, r+1)

        backtrack('', 0, 0)

        return res