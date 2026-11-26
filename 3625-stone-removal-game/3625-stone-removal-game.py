class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10: return False
        
        t=0
        for i in range(10, 0, -1):
            if n-i>=i-1:
                t=(t+1)%2
                n-=i
            else:
                break

        return t==0