class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(nums)-min(nums)*len(nums)
        
        # res=0
        # L=len(nums)

        # while len(set(nums))>1:
        #     M=max(nums)
        #     f=True
        #     for i in range(L):
        #         if nums[i]==M and f:
        #             f=False
        #             continue
        #         if f==False or nums[i]!=M:
        #             nums[i]+=1
        #     print(nums)
        #     res+=1

        # return res