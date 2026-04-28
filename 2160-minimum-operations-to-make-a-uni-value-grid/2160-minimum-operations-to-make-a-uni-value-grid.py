class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m=sorted(chain.from_iterable(grid))
        res=0
        tmp=m[len(m)//2]

        for r in grid:
            for c in r:
                if (tmp-c)%x: return -1
                
                if tmp==c:
                    continue
                elif tmp>c:
                    res+=(tmp-c)//x
                else:
                    res+=(c-tmp)//x
            
        
        return res