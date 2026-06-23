class Solution:
    def maxDistance(self, moves: str) -> int:
        d=Counter(moves)
        r=d['D']-d['U']
        c=d['R']-d['L']
        x=d['_']

        return abs(r)+abs(c)+x