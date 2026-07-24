class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        # print(list(combinations(range(1,10),2)))
        return sum(gcd(int(str(a)[0]), int(str(b)[-1]))==1 for a,b in combinations(nums, 2))