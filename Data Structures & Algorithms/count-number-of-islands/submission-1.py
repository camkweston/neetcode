
DIRECTIONS = [
    (1, 0), (0, 1), (-1, 0), (0, -1)
]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        res = 0


        def explore(r, c):
            for d_r, d_c in DIRECTIONS:
                candidate_r = r + d_r
                candidate_c = c + d_c

                if 0 <= candidate_r < rows and 0 <= candidate_c < cols and grid[candidate_r][candidate_c] == "1":
                    grid[candidate_r][candidate_c] = "X"
                    explore(candidate_r, candidate_c)




        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":
                    grid[r][c] = "X"
                    explore(r, c)
                    res += 1
        
        return res


        