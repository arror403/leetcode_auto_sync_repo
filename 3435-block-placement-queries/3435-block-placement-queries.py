class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # Coordinate compression: collect all x coordinates from queries
        coords = sorted(list(set(q[1] for q in queries)))
        mapping = {x: i for i, x in enumerate(coords)}
        n = len(coords)
        
        st = SegmentTree(n)
        # obstacles list tracks positions. 0 is the starting point (origin).
        obstacles = [0]
        results = []
        
        for q in queries:
            if q[0] == 1:
                # Type 1: Add obstacle at x
                x = q[1]
                idx = bisect.bisect_left(obstacles, x)
                prev_val = obstacles[idx - 1]
                
                # If there is a next obstacle, the gap between prev and next is split
                if idx < len(obstacles):
                    next_val = obstacles[idx]
                    st.update(mapping[next_val], next_val - x)
                
                # Add the new gap ending at x
                st.update(mapping[x], x - prev_val)
                obstacles.insert(idx, x)
                
            else:
                # Type 2: Check if block of size sz fits in [0, x]
                x, sz = q[1], q[2]
                # Find the largest obstacle <= x
                idx = bisect.bisect_right(obstacles, x)
                prev_val = obstacles[idx - 1]
                
                # Max gap is either the largest gap ending at an obstacle <= x,
                # or the gap between the last obstacle and x itself.
                max_gap_in_tree = st.query(0, mapping[x] + 1)
                max_gap = max(max_gap_in_tree, x - prev_val)
                
                results.append(max_gap >= sz)
                
        return results


class SegmentTree:
    """Iterative Segment Tree for prefix maximum queries."""
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (2 * n)

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res