class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        return requests[0]+sum(b-a if b>=a else a-b for a,b in pairwise(requests))