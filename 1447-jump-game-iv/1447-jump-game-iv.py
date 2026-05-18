class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        v = [0]*n
        p = defaultdict(list)
        for i,val in enumerate(arr): p[val].append(i)
        q = deque()
        q.append(0)
        res = 0

        while q:
            sz = len(q)
            while sz:
                sz-=1
                idx = q.popleft()
                if (idx == n-1): 
                    return res
                if (idx - 1 >= 0 and v[idx-1]==0):
                    q.append(idx-1)
                    v[idx-1] = 1
                if (idx + 1 < n and v[idx+1]==0):
                    q.append(idx+1)
                    v[idx+1] = 1
                for x in p[arr[idx]]:
                    if v[x]==0:
                        q.append(x)
                        v[x] = 1
                
                p[arr[idx]].clear()

            res+=1

        return -1