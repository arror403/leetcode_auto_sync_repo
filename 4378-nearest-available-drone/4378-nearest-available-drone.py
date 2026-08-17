class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        dx,dy=target
        res=[]

        for i, (x,y,r) in enumerate(drones):
            d=abs(dx-x)+abs(dy-y)
            if d<=r:
                res.append((d,i))


        return min(res, default=(0,-1))[1]