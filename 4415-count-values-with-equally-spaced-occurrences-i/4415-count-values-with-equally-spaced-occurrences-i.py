class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        d=defaultdict(list)
        res=0

        for i,v in enumerate(nums):
            d[v].append(i)

        for v,idx in d.items():
            if len(idx)==3:
                if idx[1]-idx[0] == idx[2]-idx[1]:
                    res+=1


        return res