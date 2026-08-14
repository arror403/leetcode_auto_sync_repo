class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l=res=0
        d=defaultdict(int)

        for r in range(len(s)):
            d[s[r]]+=1

            while d[s[r]]>2:
                d[s[l]]-=1
                l+=1
            
            res=max(res, r-l+1)


        return res