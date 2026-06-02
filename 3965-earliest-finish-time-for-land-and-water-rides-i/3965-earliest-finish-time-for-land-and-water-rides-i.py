class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res=inf

        for x,y in zip(landStartTime, landDuration):
            for p,q in zip(waterStartTime, waterDuration):
                # res=min(res, q+max(x+y, p) , y+max(p+q, x))

                if p>(x+y):
                    res=min(res, p+q)
                else:
                    res=min(res, x+y+q)

                if x>(p+q):
                    res=min(res, x+y)
                else:
                    res=min(res, p+q+y)
    

        return res