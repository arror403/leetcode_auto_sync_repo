class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while 1:
            p=reduce(operator.mul, list(map(int,str(n))))
            if p%t==0: return n
            n+=1