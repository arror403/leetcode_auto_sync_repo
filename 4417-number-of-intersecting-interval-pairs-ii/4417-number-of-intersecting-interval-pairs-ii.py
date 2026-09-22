class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals=sorted(intervals, key=lambda x:x[0])
        starts=[x[0] for x in intervals]
        res=0

        for i in range(len(intervals)):
            res += bisect_right(starts, intervals[i][1])-i-1


        return res