class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if coins<min(costs): return 0
        costs.sort()
        res=i=0
        while i<len(costs) and coins>=costs[i]:
            coins-=costs[i]
            res+=1
            i+=1

        return res