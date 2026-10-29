class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        L=len(nums)
        res=0

        for i in range(L):
            fq=[]
            pos=defaultdict(int)

            for j in range(i, L):
                x=nums[j]
                if x not in pos:
                    pos[x]=len(fq)
                    fq.append(1)
                else: 
                    fq[pos[x]]+=1

                f=True
                for t in range(len(fq)):
                    if fq[t]!=t+1:
                        f=False
                        break
                if f: res+=1

        return res