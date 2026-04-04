
class Solution:
    def decodeCiphertext(self, encoded_text: str, rows: int) -> str:
        if rows==1: return encoded_text

        L=len(encoded_text)
        cols=L//rows
        i=j=k=0
        res=[]

        while k<L:
            res.append(encoded_text[k])
            i+=1
            if i==rows:
                i=0
                j+=1
            k=i*(cols+1)+j


        return ''.join(res).rstrip()