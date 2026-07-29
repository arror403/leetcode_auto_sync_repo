class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        # Optimized by Gemma4-26B-A4B-Uncensored-HauhauCS-Balanced-Q4_K_M.gguf

        MOD = 10**9 + 7
        
        # 1. Precompute factorials and their modular inverses
        # This allows nCr % MOD to be calculated in O(1)
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = (fact[i - 1] * i) % MOD
            
        # Compute inverse factorial using Fermat's Little Theorem
        # inv_fact[n] = (fact[n]^(MOD-2)) % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, 1, -1):
            inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

        def nCr_mod(N, R):
            if R < 0 or R > N:
                return 0
            num = fact[N]
            # Denominator: (R! * (N-R)!) % MOD
            den = (inv_fact[R] * inv_fact[N - R]) % MOD
            return (num * den) % MOD

        # 2. Total sequences: Stars and Bars -> (n-1)C(k-1)
        total = nCr_mod(n - 1, k - 1)

        # 3. All-Odd sequences:
        # If (n-k) is odd, it is impossible for all k numbers to be odd.
        # If (n-k) is even, all-odd sequences = ( (n+k-2)//2 ) C (k-1)
        if (n - k) % 2 != 0:
            return total % MOD
        else:
            all_odd = nCr_mod((n + k - 2) // 2, k - 1)
            return (total - all_odd) % MOD