class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        s1, s2 = bin(a).count('1'), bin(b).count('1')
        return s1*s2 if s1>=s2 else s2//s1