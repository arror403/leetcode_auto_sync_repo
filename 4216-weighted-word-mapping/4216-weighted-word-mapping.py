class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=""
        for w in words: res+=chr(122-sum(weights[ord(s)-97] for s in w)%26)

        return res