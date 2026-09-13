class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        d=defaultdict(list)
        for i,v in enumerate(nums): d[v].append(i)
        res=0

        for v,idx in d.items():
            L=len(idx)
            if L>=3:
                diff=idx[1]-idx[0]
                c=1
                for i in range(1, L-1):
                    if idx[i+1]-idx[i] != diff: 
                        c=0
                        break
                res+=c


        return res