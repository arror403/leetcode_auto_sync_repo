class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        sides.sort()
        if (sides[0]+sides[1])<=sides[2]: return []

        res=[]
        a,b,c=sides
        # cos(x) -> acos(x) -> degree
        res.append(degrees(acos((b**2+c**2-a**2)/(2*b*c)))) # a
        res.append(degrees(acos((a**2+c**2-b**2)/(2*a*c)))) # b
        res.append(degrees(acos((a**2+b**2-c**2)/(2*a*b)))) # c

        return sorted(res)