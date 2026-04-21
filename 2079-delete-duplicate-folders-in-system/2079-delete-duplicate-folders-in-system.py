from collections import defaultdict, Counter

class TrieNode:
    def __init__(self):
        self.children = {}
        self.serial = ""

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # 1. Build the Trie
        root = TrieNode()
        for p in paths:
            cur = root
            for folder in p:
                if folder not in cur.children:
                    cur.children[folder] = TrieNode()
                cur = cur.children[folder]
        
        seen = Counter()
        
        # 2. Serialize subtrees bottom-up (Post-order traversal)
        def serialize(node):
            if not node.children:
                return ""
            
            # Create a unique signature for the current node based on its children
            # We sort child names to ensure that the same structure always results in the same string
            parts = []
            for name in sorted(node.children.keys()):
                child = node.children[name]
                # The signature for a child is "name(child_signature)"
                parts.append(f"{name}({serialize(child)})")
            
            node.serial = "".join(parts)
            seen[node.serial] += 1
            return node.serial

        serialize(root)

        # 3. Collect paths that are not marked for deletion
        res = []
        def collect(node, path):
            # If a node's serial has been seen more than once, it's a duplicate.
            # We skip this node and all its subfolders.
            if node.serial and seen[node.serial] > 1:
                return
            
            if path:
                res.append(path)
            
            for name in sorted(node.children.keys()):
                collect(node.children[name], path + [name])

        collect(root, [])
        return res