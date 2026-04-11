class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        
        # 1. Initialize a list of strings (one for each row)
        rows = [''] * numRows
        
        current_row = 0
        # True means we are going down, False means we are going up
        going_down = False 
        
        # 2. Iterate through the string and place characters into the correct row
        for char in s:
            rows[current_row] += char
            
            # Check if we need to change direction
            if current_row == 0 or current_row == numRows - 1:
                # Reverse the direction whenever we hit the top (0) or the bottom (N-1)
                going_down = not going_down
            
            # Update the row index based on the direction
            if going_down:
                current_row += 1
            else:
                current_row -= 1
                
        # 3. Join all the rows together to form the final result
        return "".join(rows)