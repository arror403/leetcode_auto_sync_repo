class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        e,o=1,0
        res=cur=0
        
        for x in arr:
            cur=(cur+x)%2
            if cur==0:
                res+=o
                e+=1
            else:
                res+=e
                o+=1
        

        return res%(10**9+7)