class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res=[]
        L=len(queries[0])

        for q in queries:
            for d in dictionary:
                diff=0
                for i in range(L):
                    diff+=(1 if q[i]!=d[i] else 0)
                    if diff>2: break
                
                if diff<=2:
                    res.append(q)
                    break


        return res