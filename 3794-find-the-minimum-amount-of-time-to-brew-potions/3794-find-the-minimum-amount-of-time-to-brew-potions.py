class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        # S[i] is the suffix sum of skills from index i to n-1
        S=list(accumulate(skill[::-1]))[::-1]+[0]
        hull = []
        x_ints = []
        # Build upper convex hull for lines y = S[j]*x - S[j+1]*y
        # Lines are added in decreasing order of slopes S[j]
        for i in range(n):
            M = S[i]
            C = -S[i+1]
            while len(hull) >= 2:
                M1, C1 = hull[-1]
                dx_new = C - C1
                dy_new = M1 - M
                dx_prev, dy_prev = x_ints[-1]
                # Check if the new intersection overtakes the previous one
                # Cross-multiply to avoid floats: dx_new / dy_new >= dx_prev / dy_prev
                if dx_new * dy_prev >= dx_prev * dy_new:
                    hull.pop()
                    x_ints.pop()
                else:
                    break
            
            if hull:
                M1, C1 = hull[-1]
                x_ints.append((C - C1, M1 - M))
            hull.append((M, C))
            
        # Base case: first potion
        ans_time = S[0] * mana[0]
        
        # Process each subsequent potion using our DP step
        for k in range(1, m):
            x = mana[k]
            y = mana[k-1]
            
            # Binary search on x_ints to find the optimal line for slope x/y
            l, r = 0, len(x_ints) - 1
            best_idx = len(x_ints)
            
            while l <= r:
                mid = (l + r) // 2
                dx, dy = x_ints[mid]
                
                # Check if intersection dx/dy >= query slope x/y
                if dx * y >= x * dy:
                    l = mid + 1
                else:
                    best_idx = mid
                    r = mid - 1
                    
            best_M, best_C = hull[best_idx]
            ans_time += best_M * x + best_C * y
            
            
        return ans_time