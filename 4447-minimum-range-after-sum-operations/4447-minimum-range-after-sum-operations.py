class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:
        t=[a, b, c]
        t.sort()

        if t[0]+t[1]<t[2]:
            return t[1]
        else:
            return t[2]-t[0]