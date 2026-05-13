class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        L=len(nums)
        m=[0]*(limit*2 + 2)
        # m=Counter()
        
        for i in range(L//2):
            l,r=nums[i],nums[L-i-1]
            # m[2]+=2
            m[min(l,r)+1]-=1
            m[l+r]-=1

            m[l+r+1]+=1
            m[max(l,r)+limit+1]+=1

        # res,cur=inf,0
        res=cur=L
        for i in range(2, limit*2 + 1):
            cur+=m[i]
            res=min(res,cur)


        return res