class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        d=Counter(nums)
        ans=[]

        for i in range(max(d.values())):
            tmp=[]
            for v in d.keys():
                if d[v]: 
                    tmp.append(v)
                    d[v]-=1
            tmp.sort()
            ans+=tmp


        return ans