class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        return ''.join([str(n) for n in nums]).count(str(digit))