class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        n='123456789'
        res=[]

        for i in range(len(n)):
            for j in range(i+1, len(n)+1):
                s=int(n[i:j])
                if s>=low and s<=high:
                    res.append(s)


        return sorted(res)