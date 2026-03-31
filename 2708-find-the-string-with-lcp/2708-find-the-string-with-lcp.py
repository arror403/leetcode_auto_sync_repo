class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        # Get the length of the string we need to construct
        L = len(lcp)
        
        # Initialize result array with 0s (0 means unassigned character)
        res = [0] * L
        
        # Start with character 1 (will map to 'a' later)
        c = 1

        # --- Step 1: Construct the string greedily ---
        for i in range(L):
            # Skip if this position already has a character assigned
            if res[i]: 
                continue
            
            # If we've exhausted all 26 letters, no valid string exists
            if c > 26: 
                return ''
            
            # For every position j >= i, if lcp[i][j] > 0, then s[i] == s[j],
            # so assign the same character to position j
            for j in range(i, L):
                if lcp[i][j]:
                    res[j] = c
            
            # Move to the next character for future unassigned positions
            c += 1
        
        # --- Step 2: Validate the constructed string against the LCP matrix ---
        for i in range(L):
            for j in range(L):
                # Get the LCP value for the suffixes starting at i+1 and j+1
                # If either i+1 or j+1 is out of bounds, the LCP is 0
                v = lcp[i + 1][j + 1] if i + 1 < L and j + 1 < L else 0
                
                # If characters at positions i and j are the same,
                # then lcp[i][j] should be lcp[i+1][j+1] + 1
                # Otherwise, lcp[i][j] should be 0
                # This follows the recurrence relation:
                #   lcp[i][j] = lcp[i+1][j+1] + 1  if s[i] == s[j]
                #   lcp[i][j] = 0                    if s[i] != s[j]
                v = v + 1 if res[i] == res[j] else 0
                
                # If the computed LCP value doesn't match the given matrix,
                # the input is invalid â no valid string exists
                if lcp[i][j] != v:
                    return ''

        # --- Step 3: Convert numeric character codes to actual letters ---
        # Map 1 -> 'a', 2 -> 'b', ..., 26 -> 'z' using ASCII offset (96 + 1 = 97 = 'a')
        return ''.join(chr(96 + i) for i in res)