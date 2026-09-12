class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # s=set()
        res=0
        L=len(timeSeries)
        for i in range(L-1):
            diff=timeSeries[i+1]-timeSeries[i]
            res+=duration if diff>duration else diff
            # s|=set(range(t, t+duration))
            # for d in range(duration):
                # s.add(t+d)

        return res+(duration if L else 0)