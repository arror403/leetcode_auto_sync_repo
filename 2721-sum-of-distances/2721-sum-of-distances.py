class Solution:
    def distance(self, nums: List[int]) -> List[int]:
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
                
                # Sum of distances to indices to the left:
                # (curr_idx - indices[0]) + (curr_idx - indices[1]) ...
                # = i * curr_idx - (sum of indices from 0 to i-1)
                left_sum_indices = prefix_sum[i-1] if i > 0 else 0
                left_dist = (i * curr_idx) - left_sum_indices
                
                # Sum of distances to indices to the right:
                # (indices[i+1] - curr_idx) + (indices[i+2] - curr_idx) ...
                # = (sum of indices from i+1 to n-1) - (count of indices to the right * curr_idx)
                right_sum_indices = total_sum - prefix_sum[i]
                count_right = n - 1 - i
                right_dist = right_sum_indices - (count_right * curr_idx)
                
                res[curr_idx] = left_dist + right_dist

        return res

        # d=defaultdict(list)
        # for i,v in enumerate(nums): d[v].append(i)

        # # print(d)
        # p={}
        # for k,v in d.items(): p[k]=list(accumulate(v))
        # # print(p)
        # res=[0]*len(nums)
        # for k,v in p.items():
        #     t=d[k]
        #     L=len(v)
        #     for i in range(L):
        #         res[t[i]]=v[-1]-(L-i-1)*v[i]+v[i]

        # return res