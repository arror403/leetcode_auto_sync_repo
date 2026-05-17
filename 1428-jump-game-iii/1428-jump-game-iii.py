class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start]==0: return True
            
        L=len(arr)
        s=set([start])

        def solve(i, v):
            if (i+v)<L:
                if arr[i+v]==0: return True
                if (i+v) not in s:
                    s.add(i+v)
                    if solve(i+v, arr[i+v]):
                        return True

            if (i-v)>=0:
                if arr[i-v]==0: return True
                if (i-v) not in s:
                    s.add(i-v)
                    if solve(i-v, arr[i-v]):
                        return True

            return False


        return solve(start, arr[start])