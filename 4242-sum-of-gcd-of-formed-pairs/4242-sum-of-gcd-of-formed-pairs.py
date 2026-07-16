class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        m=[]
        lm=-inf

        for v in nums:
            if v>lm: lm=v
            m.append(gcd(v, lm))

        d=deque(sorted(m))


        return sum(gcd(d.popleft(), d.pop()) for _ in range(len(m)>>1))