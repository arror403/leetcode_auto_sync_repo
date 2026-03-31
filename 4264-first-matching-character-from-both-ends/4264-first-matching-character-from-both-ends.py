class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        L=len(s)
        for i in range(len(s)//2):
            if s[i]==s[L-i-1]:
                return i

        if L%2: return L//2

        return -1