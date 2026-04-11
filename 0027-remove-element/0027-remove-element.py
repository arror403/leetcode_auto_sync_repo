class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ri = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ri] = nums[i]
                ri += 1
            # print(i, ri, nums[i])

        # print(nums)
        return ri