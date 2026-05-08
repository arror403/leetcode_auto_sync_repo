# Sieve of Eratosthenes to pre-calculate prime numbers up to MAX_RANGE
MAX_RANGE = (10**6) + 1
prime = [True] * MAX_RANGE
prime[0] = prime[1] = False

# The sieve algorithm to mark non-prime numbers
for i in range(2, int(sqrt(MAX_RANGE))):
    if prime[i] == True:
        for j in range(i*i, MAX_RANGE, i):
            prime[j] = False

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = 0
        val_to_index = defaultdict(list)
        for i in range(n):
            maxi = max(maxi, nums[i])
            val_to_index[nums[i]].append(i)

        visited = set()
        dist = [inf] * n
        dist[0] = 0

        q = deque()
        q.append(0)

        while q:
            node = q.popleft()
            if node - 1 >= 0 and dist[node - 1] == inf:
                q.append(node - 1)
                dist[node - 1] = 1 + dist[node]

            if node + 1 < n and dist[node + 1] == inf:
                q.append(node + 1)
                dist[node + 1] = 1 + dist[node]

            if prime[nums[node]] == False or nums[node] in visited:
                continue

            i = 1
            while True:
                new_node_val = nums[node] * i
                if new_node_val > maxi:
                    break

                for new_node_index in val_to_index[new_node_val]:
                    if dist[new_node_index] == inf:
                        q.append(new_node_index)
                        dist[new_node_index] = 1 + dist[node]

                i += 1

            visited.add(nums[node])

            if dist[n - 1] != inf: break
        

        return dist[n - 1]