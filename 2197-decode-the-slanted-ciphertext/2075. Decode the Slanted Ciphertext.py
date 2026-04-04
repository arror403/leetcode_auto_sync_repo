class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText: return ""

        L=len(encodedText)
        lr=L//rows
        t=[list(encodedText[i:i+lr]) for i in range(0, L, lr)]
        res=''
        for i in range(lr):
            x,y=0,i
            while x<rows and y<lr:
                res+=t[x][y]
                x+=1
                y+=1

        res=res.rstrip()
        return res
