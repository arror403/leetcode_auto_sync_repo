class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        # d=[[-1,-2],[-2,-1],[1,-2],[2,-1],[-2,1],[-1,2],[1,2],[2,1]]
        x, y = sum(start), sum(target)
        return ((x%2==0 and y%2==0) or (x%2!=0 and y%2!=0))