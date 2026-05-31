class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        return sum(int(x) for x in str(n))