class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        p=[[0]*n for _ in range(m)]
        d={'R':(0,1), 'D':(1,0), 'L':(0,-1), 'U':(-1,0)}
        i=j=0

        while 1:
            p[i][j]=1
            x, y = i + d[grid[i][j]][0], j + d[grid[i][j]][1]

            if x not in range(m) or y not in range(n) or p[x][y]:
                return [i,j]

            i,j=x,y