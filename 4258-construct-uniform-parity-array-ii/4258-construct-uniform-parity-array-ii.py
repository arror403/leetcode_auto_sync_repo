class Solution:
    def uniformArray(self, arr: list[int]) -> bool:
        r=[0,0]
        m=inf
        for v in arr: 
            r[v%2]+=1
            if v%2: m=min(m,v)

        L=len(arr)
        if r[0]==L or r[1]==L: return True

        for v in arr:
            if v%2==0 and (v-m)<1: 
                return False


        return True