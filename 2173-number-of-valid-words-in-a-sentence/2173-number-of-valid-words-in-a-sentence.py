class Solution:
    def countValidWords(self, sentence: str) -> int:
        res=0
        r=re.compile('^[a-z]*([a-z]+\-[a-z]+)?[a-z]*[\!\.\,]?$')
        for s in sentence.split():
            # print(r.match(s))
            if r.match(s):
                res+=1

        return res