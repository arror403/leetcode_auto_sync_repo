class Solution:
    def passwordStrength(self, password: str) -> int:
        res=0
        for s in set(password):
            if s.islower(): res+=1
            elif s.isupper(): res+=2
            elif s.isnumeric(): res+=3
            else: res+=5

        return res