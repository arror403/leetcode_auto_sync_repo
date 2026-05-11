class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return list(map(int, ''.join([str(x) for x in nums])))