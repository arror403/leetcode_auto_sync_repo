class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        res=1
        # t=[]
        s=list(set(nums))
        for a,b in combinations(s, 2):
            # t.append(lcm(a,b)*gcd(a,b))
            res=max(res, (a*b)/(gcd(a,b))**2)

        # print(t)
        return int(res)