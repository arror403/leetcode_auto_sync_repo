class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        d=defaultdict(int)
        for a,b in zip(s1, s2):
            if a!=b:
                d[(a,b)]+=1
        # print(d)
        if sum(d.values())%2: return -1

        else: return d[('x','y')]//2 + d[('y','x')]//2 + (d[('x','y')]%2)*2