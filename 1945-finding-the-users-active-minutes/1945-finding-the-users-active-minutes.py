class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d=defaultdict(set)
        res=[0]*k

        for x,v in logs: d[x].add(v)

        for x in d.values(): res[len(x)-1]+=1


        return res