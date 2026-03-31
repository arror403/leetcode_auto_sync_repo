class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
        size=[1]*n
        parity=[0]*n
        parent=[i for i in range(n)]
        count=0

        def find(x):
            if parent[x]==x: return [x, 0]

            [root, par] = find(parent[x])
            parent[x] = root
            parity[x] ^= par

            return [parent[x], parity[x]]

        def unite(u, v, w):
            [pu, xu] = find(u)
            [pv, xv] = find(v)

            if pu == pv:
                # check if adding edge keeps cycle even
                return ((xu ^ xv) == w)
            # unite by size
            if size[pu] < size[pv]:
                pu, pv = pv, pu 
                xu, xv = xv, xu
            parent[pv] = pu
            # set parity
            parity[pv] = xu ^ xv ^ w
            size[pu] += size[pv]

            return True


        for u, v, w in edges:
            if unite(u, v, w):
                count+=1

        return count     