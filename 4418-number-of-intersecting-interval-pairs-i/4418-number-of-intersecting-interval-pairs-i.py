class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        res=0
        for a, b in combinations(map(tuple, intervals), 2):
            if set(range(a[0], a[1]+1)) & set(range(b[0], b[1]+1)): 
                res+=1

        return res