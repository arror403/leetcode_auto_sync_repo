class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # t=sum(a[0] for a in tasks)
        tasks.sort(key=lambda x:x[1]-x[0], reverse=True)
        # print(tasks)
        cur=ini=0

        for a,b in tasks:
            if cur<b:
                ini+=(b-cur)
                cur=b
            cur-=a

        return ini