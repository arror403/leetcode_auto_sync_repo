class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n=len(nums)
        d=defaultdict(list)
        B=isqrt(n)
        MOD=(10**9+7)

        for q in queries:
            l,r,k,v=q
            if k>=B:
                for i in range(l, r+1, k):
                    nums[i]=(nums[i]*v)%MOD
            else:
                d[k].append(q)

        for k, Q in d.items():
            diff=[1]*n 
            for q in Q:
                l, r, _, v = q
                # Multiply starting position
                diff[l]=(diff[l]*v)%MOD
                # Cancel the multiplication using modular inverse
                nxt = l + ((r-l)//k + 1) * k
                if nxt < n:
                    # pow(v, -1, MOD) computes the modular inverse natively
                    diff[nxt] = (diff[nxt] * pow(v, -1, MOD)) % MOD
            # Propagate the multipliers with a step size of k
            for i in range(n):
                if i >= k:
                    diff[i] = (diff[i] * diff[i - k]) % MOD
                nums[i] = (nums[i] * diff[i]) % MOD


        return reduce(xor, nums)