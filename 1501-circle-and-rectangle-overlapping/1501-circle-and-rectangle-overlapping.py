class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        def f(i, j, k):
            if i<=k<=j:
                return 0
            return i-k if k<i else k-j

        a = f(x1, x2, xCenter)
        b = f(y1, y2, yCenter)
        
        
        return a**2 + b**2 <= radius**2