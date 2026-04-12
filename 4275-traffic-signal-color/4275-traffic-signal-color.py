class Solution:
    def trafficSignal(self, timer: int) -> str:
        if timer==0: return 'Green'
        elif timer==30: return'Orange'
        elif timer in range(31,91): return 'Red'
        else: return 'Invalid'