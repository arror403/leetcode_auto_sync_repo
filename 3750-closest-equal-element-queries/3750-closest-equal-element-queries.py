class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        ## using llama-b8795-bin-win-vulkan-x64 (llama-server) gemma-4-26B-A4B-it-UD-Q4_K_M.gguf 

        n = len(nums)
        # Step 1: Group indices by their value
        pos_map = defaultdict(list)
        for i, val in enumerate(nums):
            pos_map[val].append(i)
        
        # Step 2: Pre-calculate the minimum distance for each index
        # min_dist_map[index] will store the result for that index
        min_dist_map = {}
        
        for val, indices in pos_map.items():
            k = len(indices)
            if k == 1:
                # If the number appears only once, distance is -1
                min_dist_map[indices[0]] = -1
                continue
            
            # To handle circularity easily, we can calculate gaps
            # gaps[i] is the distance between indices[i] and indices[i+1]
            gaps = []
            for i in range(k - 1):
                gaps.append(indices[i+1] - indices[i])
            # The last gap is the circular wrap-around distance
            gaps.append(n - indices[k-1] + indices[0])
            
            for i in range(k):
                # The distance for indices[i] is the minimum of 
                # the gap to its left and the gap to its right.
                # The gap to the left of indices[i] is gaps[i-1]
                # The gap to the right of indices[i] is gaps[i]
                left_gap = gaps[i-1] # if i=0, i-1 is k-1 (the wrap-around gap)
                right_gap = gaps[i]
                min_dist_map[indices[i]] = min(left_gap, right_gap)
                
        # Step 3: Answer the queries
        answer = []
        for q in queries:
            answer.append(min_dist_map[q])
            
        return answer

        # d=defaultdict(list)
        # for i in range(len(nums)):
        #     d[nums[i]].append(i)

        # for q in queries:
        #     a=bisect_right(d[nums[q]], nums[q])
        #     b=bisect_left(d[nums[q]], nums[q])
        #     print(a,b)
        # print(d)

        # return []