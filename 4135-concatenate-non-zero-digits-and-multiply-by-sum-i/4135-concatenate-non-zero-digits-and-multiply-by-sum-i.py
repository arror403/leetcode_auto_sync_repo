class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=[v for v in map(int,str(n)) if v!=0]
        
        return sum(x)*int(''.join(str(v) for v in x)) if x else 0