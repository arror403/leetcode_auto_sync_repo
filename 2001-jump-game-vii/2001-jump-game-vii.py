class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        Uses dynamic programming with a sliding window to track the number 
        of reachable indices within the valid jump range [i - maxJump, i - minJump].
        """
        n = len(s)
        # dp[i] stores whether index i is reachable
        dp = [False] * n
        dp[0] = True
        
        # count tracks the number of reachable '0's in the current window
        count = 0
        
        for i in range(1, n):
            # Add the index entering the window: i - minJump
            if i >= minJump:
                if dp[i - minJump]:
                    count += 1
            
            # Remove the index leaving the window: i - maxJump - 1
            if i > maxJump:
                if dp[i - maxJump - 1]:
                    count -= 1
            
            # Current index is reachable if it is '0' and there's a reachable index in range
            if s[i] == '0' and count > 0:
                dp[i] = True
                
                
        return dp[n - 1]