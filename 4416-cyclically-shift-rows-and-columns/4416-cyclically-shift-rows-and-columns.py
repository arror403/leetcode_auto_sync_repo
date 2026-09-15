class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        
        for i in range(n):
            tmp=grid[i]
            grid[i]=tmp[rowShift[i]:]+tmp[:rowShift[i]]

        grid=list(zip(*grid))

        for i in range(n):
            tmp=grid[i]
            grid[i]=tmp[colShift[i]:]+tmp[:colShift[i]]


        return list(zip(*grid))