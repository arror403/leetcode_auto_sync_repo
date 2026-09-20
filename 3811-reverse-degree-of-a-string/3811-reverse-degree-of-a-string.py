class Solution:
    def reverseDegree(self, s: str) -> int:
        res=0
        i=1

        for c in s:
            res+=(123-ord(c))*i
            i+=1


        return res    