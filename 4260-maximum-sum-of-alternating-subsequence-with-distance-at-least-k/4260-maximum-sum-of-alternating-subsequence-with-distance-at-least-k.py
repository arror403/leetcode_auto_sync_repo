class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Using a constant max value for Fenwick Trees.
        MAX_V = 100000
        
        # bit_down stores maximum dp_down values, queried for prefix maximums (nums[j] < nums[i]).
        bit_down = [0] * (MAX_V + 2)
        # bit_up stores maximum dp_up values, queried for suffix maximums (nums[j] > nums[i]).
        # To use standard BIT for suffix max, we use a reversed index: (MAX_V - val + 1).
        bit_up = [0] * (MAX_V + 2)

        # dp_up[i] stores max score of alternating subsequence ending at i where nums[i] is a peak.
        # dp_down[i] stores max score where nums[i] is a valley.
        dp_up = [0] * n
        dp_down = [0] * n
        
        res = 0
        
        for i in range(n):
            # Once the index i-k becomes available, update the Fenwick Trees.
            # This ensures the distance condition (i - j >= k).
            if i >= k:
                prev_idx = i - k
                v_prev = nums[prev_idx]
                val_up = dp_up[prev_idx]
                val_down = dp_down[prev_idx]
                
                # Update bit_down with dp_down[prev_idx] at index v_prev
                idx = v_prev
                while idx <= MAX_V:
                    if val_down > bit_down[idx]:
                        bit_down[idx] = val_down
                        idx += idx & (-idx)
                    else:
                        # Optimization: Since we only ever increase values, if val is not
                        # larger than the current max in the BIT node, it won't affect the rest.
                        break
                
                # Update bit_up with dp_up[prev_idx] using reversed index
                idx = MAX_V - v_prev + 1
                while idx <= MAX_V:
                    if val_up > bit_up[idx]:
                        bit_up[idx] = val_up
                        idx += idx & (-idx)
                    else:
                        break
            
            v_curr = nums[i]
            
            # Calculate dp_up[i]: nums[i] is a peak, so previous was a valley and nums[j] < nums[i]
            res_down = 0
            idx = v_curr - 1
            while idx > 0:
                if bit_down[idx] > res_down:
                    res_down = bit_down[idx]
                idx -= idx & (-idx)
            dp_up[i] = v_curr + res_down
            
            # Calculate dp_down[i]: nums[i] is a valley, so previous was a peak and nums[j] > nums[i]
            res_up = 0
            idx = MAX_V - (v_curr + 1) + 1
            # If v_curr + 1 > MAX_V, idx will be <= 0, loop won't run
            while idx > 0:
                if bit_up[idx] > res_up:
                    res_up = bit_up[idx]
                idx -= idx & (-idx)
            dp_down[i] = v_curr + res_up
            
            # Update global maximum score
            if dp_up[i] > res: res = dp_up[i]
            if dp_down[i] > res: res = dp_down[i]
                

        return res