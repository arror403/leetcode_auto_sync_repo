class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res=0
        d=defaultdict(list)
        for i,c in enumerate(word): d[c].append(i)
        
        s=set()
        for c in word:
            if c.islower():
                s.add(c)

        for c in s:
            C=c.upper()
            if C in d:
                upper_i=d[C]
                lower_i=d[c]

                if all(i<upper_i[0] for i in lower_i):
                    res+=1


        return res