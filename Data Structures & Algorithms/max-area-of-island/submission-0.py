class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        DIRECTIONS = [
            (1, 0), (0, 1), (-1, 0), (0, -1)
        ]

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])


        res = 0


        def explore(r, c):
            area = 1
            for d_r, d_c in DIRECTIONS:
                c_r = r + d_r
                c_c = c + d_c

                if 0 <= c_r < rows and 0 <= c_c < cols and grid[c_r][c_c] == 1:
                    grid[c_r][c_c] = "X"
                    area += explore(c_r, c_c)
            
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = "X"
                    res = max(res, explore(r, c))
        
        return res
        