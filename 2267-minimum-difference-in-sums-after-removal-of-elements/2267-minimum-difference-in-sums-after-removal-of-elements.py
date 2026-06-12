class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n=len(nums)//3
        diff=[0]*(n+1)
        pqL=[-x for x in nums[:n]]
        heapify(pqL)
        pqR=nums[2*n:]
        heapify(pqR)
        S=sum(nums[:n])
        res=S

        for i in range(n, 2*n+1):
            diff[i-n]=S
            x=nums[i]
            if x>=-pqL[0]: continue
            S+=x+pqL[0]
            heapreplace(pqL, -x)

        S=sum(nums[2*n:])
        res-=S
        for i in range(2*n-1, n-2, -1):
            diff[i-n+1]-=S
            res=min(res, diff[i-n+1])
            x=nums[i]
            if x<=pqR[0]: continue
            S+=x-pqR[0]
            heapreplace(pqR, x)


        return res