class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [r[:] for r in grid]
        num_layers = min(m // 2, n // 2)

        for i in range(num_layers):
            top_row = i
            bottom_row = m - 1 - i
            left_col = i
            right_col = n - 1 - i
            layer_values = []
            layer_coords = []
            
            for j in range(left_col, right_col + 1):
                layer_values.append(res[top_row][j])
                layer_coords.append((top_row, j))
            
            for j in range(top_row + 1, bottom_row + 1):
                layer_values.append(res[j][right_col])
                layer_coords.append((j, right_col))

            for j in range(right_col - 1, left_col - 1, -1):
                layer_values.append(res[bottom_row][j])
                layer_coords.append((bottom_row, j))

            for j in range(bottom_row - 1, top_row, -1):
                layer_values.append(res[j][left_col])
                layer_coords.append((j, left_col))
            
            P = len(layer_values)
            if P == 0:
                continue
                
            k_prime = k % P
            if k_prime != 0:
                rotated_values = layer_values[k_prime:] + layer_values[:k_prime]
                for idx in range(P):
                    r, c = layer_coords[idx]
                    res[r][c] = rotated_values[idx]
                    

        return res