class Solution:
    def maxRepOpt1(self, text: str) -> int:
        d=Counter(text)
        t=[(k, len(list(g))) for k,g in groupby(text)]
        # length of the longest substring +1
        res=max(min(l+1, d[k]) for k,l in t)

        # two substring(same character) seperated by one different
        for i in range(1, len(t)-1):
            if t[i-1][0]==t[i+1][0] and t[i][1]==1:
                res=max(res, min(t[i-1][1]+t[i+1][1]+1, d[t[i+1][0]]))


        return res