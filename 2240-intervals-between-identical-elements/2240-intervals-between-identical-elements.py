class Solution:
    def getDistances(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        for i, v in enumerate(nums):
            d[v].append(i)

        res = [0] * len(nums)
        
        for val, indices in d.items():
            n = len(indices)
            if n < 2:
                continue
            
            prefix_sum = list(accumulate(indices))
            total_sum = prefix_sum[-1]

            for i in range(n):
                curr_idx = indices[i]
                
                left_sum_indices = prefix_sum[i-1] if i > 0 else 0
                left_dist = (i * curr_idx) - left_sum_indices
                
                right_sum_indices = total_sum - prefix_sum[i]
                count_right = n - 1 - i
                right_dist = right_sum_indices - (count_right * curr_idx)
                
                res[curr_idx] = left_dist + right_dist


        return res