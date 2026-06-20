class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        lim = sorted([[0,0]]+[[r[0]-1,r[1]] for r in restrictions])
        
        for i in range(1, len(lim)):
            idx, h = lim[i]
            pi, ph = lim[i-1]
            h = min(h, ph+(idx-pi))
            lim[i][1] = h

        for i in range(len(lim)-2, -1, -1):
            idx, h = lim[i]
            ni, nh = lim[i+1]
            h = min(h, nh+ni-idx)
            lim[i][1] = h

        res = 0
        for i in range(len(lim)-1):
            idx1, h1 = lim[i]
            idx2, h2 = lim[i+1]
            peak = (h1+h2+idx2-idx1)//2
            res = max(res, peak, h1, h2)
            

        return max(res, lim[-1][1]-lim[-1][0]+n-1)