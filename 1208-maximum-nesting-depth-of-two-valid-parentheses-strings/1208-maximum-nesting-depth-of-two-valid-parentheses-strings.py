class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        return [i&1^(seq[i]=='(') for i in range(len(seq))]