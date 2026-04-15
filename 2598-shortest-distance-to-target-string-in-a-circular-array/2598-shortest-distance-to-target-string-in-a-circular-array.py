class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        L=len(words)
        i=startIndex
        d=[]

        for _ in range(L):
            if words[i]==target:
                d.append(min(abs(i-startIndex), L-abs(i-startIndex)))

            i=(i+1)%L
            

        return min(d) if d else -1