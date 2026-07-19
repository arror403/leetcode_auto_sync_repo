class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # d=dict.fromkeys(s)
        t=set()
        st=[]
        d={}
        for i in range(len(s)): d[s[i]]=i

        for i in range(len(s)):
            if s[i] not in t:
                while st and s[i]<st[-1] and i<d[st[-1]]:
                    t.remove(st.pop())
                    
                t.add(s[i])
                st.append(s[i])


        return ''.join(st)