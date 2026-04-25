class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
    # import sys
    # sys.setrecursionlimit(3000)
        # --- Step 1: Calculate Critical Path Indices (K_i) ---
        critical_indices = []
        r_coord, c_coord = 0, 0
        # P0 (Start cell)
        critical_indices.append(r_coord * 4 + c_coord)
        # P1 through P6 (6 moves)
        for move in directions:
            if move == 'D':
                r_coord += 1
            else: # move == 'R'
                c_coord += 1
            # Note: Since the path length is 7 (0 to 6), we check 6 moves
            critical_indices.append(r_coord * 4 + c_coord)
        # Convert the list of critical indices to a set for fast lookup
        critical_indices_set = set(critical_indices)
        # --- Step 2: Digit DP Setup ---
        memo = {}
        
        def dp(idx, tight, prev_critical_digit, N_str):
            """
            Counts the number of ways to complete the 16-digit number S
            satisfying the constraints defined by N_str and the path requirements.
            """
            if idx == 16:
                # Successfully formed a valid 16-digit number
                return 1
            state = (idx, tight, prev_critical_digit)
            if state in memo:
                return memo[state]
            # Determine the upper limit for the current digit
            limit = int(N_str[idx]) if tight else 9
            
            count = 0
            
            for d in range(limit + 1):
                # 1. Check Path Constraint
                is_critical = idx in critical_indices_set
                
                next_prev_critical_digit = prev_critical_digit
                valid = True

                if is_critical:
                    if prev_critical_digit == -1:
                        # This is K0. Start of the sequence.
                        next_prev_critical_digit = d
                    else:
                        # This is Ki (i > 0). Must be non-decreasing.
                        if d < prev_critical_digit:
                            valid = False
                        else:
                            next_prev_critical_digit = d
                
                if valid:
                    # 2. Calculate new tight constraint
                    new_tight = tight and (d == limit)
                    # 3. Recurse
                    count += dp(idx + 1, new_tight, next_prev_critical_digit, N_str)
            
            memo[state] = count
            return count

        def count_good_le_N(N):
            if N < 0:
                return 0
            # Convert N to a 16-digit string, ensuring leading zeros
            N_str = str(N).zfill(16)
            # Clear memoization for each run
            memo.clear()
            # Initial call: idx=0, tight=True, prev_critical_digit=-1 (sentinel value)
            return dp(0, True, -1, N_str)

        # --- Step 3: Calculate Result ---
        # Count numbers <= r
        count_r = count_good_le_N(r)
        # Count numbers <= l-1
        count_l_minus_1 = count_good_le_N(l - 1)
        
        return count_r - count_l_minus_1