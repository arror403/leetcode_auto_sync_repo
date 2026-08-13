class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c)<k: return max(self.longestSubstring(t, k) for t in s.split(c))

        return len(s)

        # res=0
        # d=Counter(s[:k])
        # if all(x>=k for x in d.values()): res+=1
        
        # for i in range(len(s)-k):
        #     print(s[i],s[i+k])
        #     d[s[i]]-=1
        #     d[s[i+k]]+=1
        #     print(s[i:i+k])

        #     if all(x>=k for x in d.values()):
        #         res+=1

        # print(s[len(s)-k:])
        # if all(x>=k for x in Counter(s[len(s)-k:]).values()): res+=1

        # return res