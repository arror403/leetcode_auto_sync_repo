class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        d=defaultdict(int)
        
        for i in range(len(nums)-k+1):
            for v in set(nums[i:i+k]):
                d[v]+=1
        
        
        return max([-1]+[v for v,f in d.items() if f==1])