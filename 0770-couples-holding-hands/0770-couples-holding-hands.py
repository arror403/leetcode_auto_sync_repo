class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        L = len(row)
        res = 0
        p = {}
        for i in range(L): p[row[i]] = i

        for i in range(0, L, 2):
            c1, c2 = row[i], row[i+1]
            if (c1%2==0 and c2!=c1+1) or (c1&1 and c2!=c1-1):
                source_int = row[i]
                target_pos = p[source_int-1] if source_int&1 else p[source_int+1]
                row[i+1], row[target_pos] = row[target_pos], row[i+1]
                p[row[i+1]], p[row[target_pos]] = i+1, target_pos
                res += 1


        return res