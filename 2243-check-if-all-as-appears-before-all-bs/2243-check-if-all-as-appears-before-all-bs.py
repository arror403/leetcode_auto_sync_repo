class Solution:
    def checkString(self, s: str) -> bool:
        return sorted(s)==list(s)