class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:

        # by gemma-4-E4B-it-Q5_K_M.gguf

        n = len(nums)
        MOD = 10**9 + 7
        
        # Group queries by their stride k, separating small and large k
        small_k_queries = defaultdict(list)
        
        # B determines the threshold for square root decomposition
        B = math.isqrt(n)

        # 1. Process Large K Queries (k >= B)
        # These are handled directly as they affect few elements.
        for q in queries:
            l, r, k, v = q
            if k >= B:
                # Direct update for large strides
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % MOD
            else:
                # Store queries for small strides
                small_k_queries[k].append(q)

        # 2. Process Small K Queries (k < B)
        # These are handled using a dynamic programming/difference array approach.
        for k, q_list in small_k_queries.items():
            
            # diff[i] stores the total multiplicative factor applied to nums[i] 
            # due to the small stride k. Initialize to 1.
            diff = [1] * n 
            
            # First pass: Calculate multiplicative factors for starting points of intervals
            for l, r, _, v in q_list:
                
                # Apply v at the start of the interval
                diff[l] = (diff[l] * v) % MOD
                
                # Determine the index immediately after the last index divisible by k 
                # that is within the query range [l, r].
                # This effectively marks the end of the influence range for this specific query.
                
                # The number of full steps of k in [l, r] is floor((r - l) / k) + 1
                # The index *after* this last step is:
                nxt = l + ((r - l) // k + 1) * k
                
                if nxt < n:
                    # Apply the inverse of v at the stopping point.
                    # pow(v, -1, MOD) calculates modular inverse
                    try:
                        inverse_v = pow(v, -1, MOD)
                        diff[nxt] = (diff[nxt] * inverse_v) % MOD
                    except ValueError:
                        # Handle case where v is not invertible (e.g., v=0, though unlikely 
                        # in typical competitive programming scenarios involving MOD arithmetic)
                        pass 

            # Second pass: Apply the multiplicative factor across the stride k
            # This step implements the dependency: diff[i] depends on diff[i-k]
            for i in range(k, n):
                # This step aggregates the factors: diff[i] = diff[i] * diff[i-k]
                diff[i] = (diff[i] * diff[i - k]) % MOD
            
            # Apply the final calculated factors to the original array
            for i in range(n):
                nums[i] = (nums[i] * diff[i]) % MOD

        # 3. Return the XOR sum of the final array
        return reduce(lambda x, y: x ^ y, nums)