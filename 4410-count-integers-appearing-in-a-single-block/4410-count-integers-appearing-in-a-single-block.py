class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        d=defaultdict(int)

        for k,_ in groupby(nums): d[k]+=1

        return sum(x==1 for x in d.values())