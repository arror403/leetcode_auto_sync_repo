class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = 0

        for l, u in zip(ascii_lowercase, ascii_uppercase):
            if l not in word or u not in word: continue
            res += word.rfind(l) < word.find(u)


        return res