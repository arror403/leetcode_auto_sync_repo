class Solution:
    def smallestPalindrome(self, s: str) -> str:
        L=len(s)
        d=sorted(s[:L//2])
        
        return ''.join(d+[s[L//2]]+d[::-1]) if L%2 else ''.join(d+d[::-1])