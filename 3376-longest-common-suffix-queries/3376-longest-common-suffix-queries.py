class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        class TrieNode:
            __slots__ = 'children', 'best_idx'
            def __init__(self):
                self.children = {}
                self.best_idx = -1

        root = TrieNode()
        lens = [len(w) for w in wordsContainer]

        def update(node, idx, length):
            if node.best_idx == -1:
                node.best_idx = idx
                return
            prev_len = lens[node.best_idx]
            if length < prev_len or (length == prev_len and idx < node.best_idx):
                node.best_idx = idx

        for i, w in enumerate(wordsContainer):
            node = root
            update(node, i, lens[i])
            for c in reversed(w):
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
                update(node, i, lens[i])

        res = []
        for q in wordsQuery:
            node = root
            best = root.best_idx
            for c in q[::-1]:
                if c in node.children:
                    node = node.children[c]
                    best = node.best_idx
                else:
                    break
            res.append(best)

            
        return res