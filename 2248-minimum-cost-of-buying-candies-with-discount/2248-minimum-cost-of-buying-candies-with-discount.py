class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        cost.reverse()
        L=len(cost)
        r=L%3
        res=0

        if r==1: res+=cost[-1]
        elif r==2: res+=cost[-1]+cost[-2]
        
        for i in range(0, (L-r), 3):
            res+=cost[i]+cost[i+1]


        return res