class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        # at your left and bigger than you
        # at your right and smaller than you
        n=len(nums)
        prefMax=[0]*n
        sufMin=[0]*n
        prefMax[0]=nums[0]
        sufMin[-1]=nums[-1]

        for i in range(1, n):
            prefMax[i]=max(prefMax[i-1], nums[i])
            sufMin[n-1-i]=min(sufMin[n-i], nums[n-1-i])

        res=[0]*n
        res[-1]=prefMax[-1]
        for i in range(n-2,-1,-1):
            if prefMax[i]>sufMin[i+1]:
                res[i]=max(prefMax[i], res[i+1])
            else: 
                res[i]=prefMax[i]


        return res