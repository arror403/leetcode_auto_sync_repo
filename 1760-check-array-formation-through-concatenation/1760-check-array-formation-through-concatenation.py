class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        l=L=len(arr)

        for p in pieces:
            if p[0] not in arr: return False
            i=arr.index(p[0])
            for x in p:
                if (i not in range(l)) or x!=arr[i]: return False
                else:
                    L-=1
                    i+=1
     

        return L==0