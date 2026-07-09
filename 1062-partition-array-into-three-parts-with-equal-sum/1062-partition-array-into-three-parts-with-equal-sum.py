class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s=sum(arr)
        if s%3: return False
        s//=3
        t=p=0
        for i in range(len(arr)):
            t+=arr[i]
            if t==s:
                t=0
                p+=1
            # if p==2:
                # return sum(arr[i+1:])==s

        return p>=3