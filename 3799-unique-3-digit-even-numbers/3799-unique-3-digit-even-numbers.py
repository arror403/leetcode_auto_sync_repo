class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        return len({x[0]*100+x[1]*10+x[2] for x in permutations(digits, 3) if x[0] and x[2]%2==0})