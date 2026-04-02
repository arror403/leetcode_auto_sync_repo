class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        f = [0]*n
        
        for j in range(m):
            now = 0
            for i in range(n):
                now = max(now, f[i]) + skill[i] * mana[j]
            f[n - 1] = now
            for i in range(n - 2, -1, -1):
                f[i] = f[i+1] - skill[i+1] * mana[j]


        return f[n - 1]