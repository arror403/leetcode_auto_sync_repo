class Solution:
    def rotatedDigits(self, n: int) -> int:
        rotated_same_nums = set([0, 1, 8])
        rotated_valid_nums = set([0, 1, 8, 2, 5, 6, 9])
        s = set()
        res = 0
        digits = list(map(int, str(n)))
        L = len(digits)

        for i, digit in enumerate(digits):
            for d in range(digit):
                if s <= rotated_valid_nums and d in rotated_valid_nums:
                    res += 7**(L - i - 1)
                if s <= rotated_same_nums and d in rotated_same_nums:
                    res -= 3**(L - i - 1)

            if digit not in rotated_valid_nums:
                return res

            s.add(digit)


        return res + (s <= rotated_valid_nums and not (s <= rotated_same_nums))