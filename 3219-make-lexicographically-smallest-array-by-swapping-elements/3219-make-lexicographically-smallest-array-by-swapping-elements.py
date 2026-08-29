class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        b = sorted([[v, i] for i, v in enumerate(nums)], key = lambda x : x[0])
        c = [[b[0]]]

        for i in range(1, len(nums)):
            if b[i][0] - b[i-1][0] <= limit:
                c[-1].append(b[i])
            else:
                c.append([b[i]])

        for t in c:
            for i, v in enumerate(sorted(p[1] for p in t)):
                nums[v] = t[i][0]


        return nums