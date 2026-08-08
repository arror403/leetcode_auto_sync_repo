class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.parent = list(range(len(s)))
        for a, b in pairs:
            self.union(a, b)

        G = defaultdict(lambda: ([], []))  
        for i, c in enumerate(s):
            parent = self.find(i)
            G[parent][0].append(i)
            G[parent][1].append(c)

        res = [''] * len(s)
        for ids, chars in G.values():
            ids.sort()
            chars.sort()
            for c, i in zip(chars, ids):
                res[i] = c
                
        return ''.join(res)


    def union(self, a, b):
        self.parent[self.find(a)] = self.find(b)
		

    def find(self, a):
        if self.parent[a] != a: self.parent[a] = self.find(self.parent[a])
        return self.parent[a]