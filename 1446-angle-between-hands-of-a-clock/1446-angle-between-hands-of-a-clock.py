class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        t=abs(hour*30-minutes*5.5)
        return min(t, 360-t)