class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        discounts.sort()
        discounts=discounts[::-1]
        prices.sort()
        prices=prices[::-1]
        res=0.0
        t=min(len(prices), len(discounts))

        for i in range(t):
            res+=prices[i]*(100-discounts[i])/100
        
        return res+sum(prices[t:])