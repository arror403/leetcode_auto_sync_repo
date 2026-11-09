class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        res=[]
        t1=t2=''

        for a,b in zip(s1, s2):
            if a==b:
                if t1 and t2:
                    res.append([t1,t2])
                    t1=t2=''
                else:
                    continue
            else:
                t1+=a
                t2+=b

        if t1 and t2: res.append([t1,t2])


        return res