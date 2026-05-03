class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        t=[v%2 for v in nums]
        L=len(nums)
        res=[]

        for i in range(L):
            s=0
            for j in range(i+1, L):
                if (t[i]+t[j])==1:
                    s+=1
            res.append(s)


        return res