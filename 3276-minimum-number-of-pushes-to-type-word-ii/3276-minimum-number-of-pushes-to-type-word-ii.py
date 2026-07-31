class Solution:
    def minimumPushes(self, word: str) -> int:
        d=sorted(Counter(word).items(), key=lambda x:x[1], reverse=True)
        res=0
        for i in range(len(d)):
            if i<8:
                res+=d[i][1]
            elif i<16:
                res+=d[i][1]*2
            elif i<24:
                res+=d[i][1]*3
            else:
                res+=d[i][1]*4

        return res