class Solution:
    def maxSumOfSquares(self, num: int, s: int) -> str:
        if s > 9*num: return ''

        q, r = s//9, s%9

        return '9'*q+str(r)+'0'*(num-q-1) if r else '9'*q+'0'*(num-q)