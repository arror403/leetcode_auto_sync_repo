class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        d=Counter(barcodes)
        i,L=0,len(barcodes)
        res=[0]*L

        for v,f in d.most_common():
            for _ in range(f):
                if i>=L:
                    i=1
                res[i]=v
                i+=2


        return res