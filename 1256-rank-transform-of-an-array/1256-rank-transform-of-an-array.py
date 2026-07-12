class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        t=sorted(dict.fromkeys(arr))
        R={t[i]:i+1 for i in range(len(t))}
        return [R[v] for v in arr]