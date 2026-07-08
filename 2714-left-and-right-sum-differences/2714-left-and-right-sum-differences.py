class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        a=nums[:]
        a.insert(0,0)
        a=list(itertools.accumulate(a))
        a.pop()
        # print(a)
        b=nums[:]
        b.reverse()
        b.insert(0,0)
        b=list(itertools.accumulate(b))
        b.pop()
        b.reverse()
        # print(b)

        return [abs(a[i]-b[i]) for i in range(len(nums))]
