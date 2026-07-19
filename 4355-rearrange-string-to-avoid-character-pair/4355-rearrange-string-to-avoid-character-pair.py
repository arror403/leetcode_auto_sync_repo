class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        f = s.count(y) 
        return y*f + s.replace(y, '')