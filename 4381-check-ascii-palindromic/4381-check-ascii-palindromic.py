class Solution:
    def isPalindromic(self, s: str) -> bool:
        t=''.join((bin(ord(c))[2:]).zfill(8) for c in s)

        return t==t[::-1]