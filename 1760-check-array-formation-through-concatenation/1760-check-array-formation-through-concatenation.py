class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d={x[0]:x for x in pieces}
        res=[]
        
        for v in arr: res+=d.get(v, [])

        return res==arr