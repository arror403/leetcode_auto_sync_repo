class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        d={x:sum(list(map(int,str(x)))) for x in nums}
        t=sorted(nums, key=lambda x:(d[x], x))
        L=len(nums)
        pos={nums[i]:i for i in range(L)}
        swaps=0

        for i in range(L):
            if t[i] != nums[i]:
                ind = pos[t[i]]
                nums[i], nums[ind] = nums[ind], nums[i]
                pos[nums[i]] = i
                pos[nums[ind]] = ind
                swaps += 1


        return swaps