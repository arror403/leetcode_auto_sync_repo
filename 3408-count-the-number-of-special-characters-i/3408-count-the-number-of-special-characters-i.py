class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s=set(word)
        return sum([w.isupper() and w.lower() in s for w in s])