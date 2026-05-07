
DIRECTIONS = [
    (1,0), (0, 1), (-1, 0), (0, -1)
]

from collections import deque

class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:

        # iterate through all the nodes in the grid
        
        # once you see a 1 do a DFS 

        # mark each node as a X and increment res

        if not grid:
            return 0

        res = 0
        ROWS, COLS = len(grid), len(grid[0])


        # def dfs(curr_r, curr_c):
        #     grid[curr_r][curr_c] = "X"
        #     for dr,dc in DIRECTIONS:
        #         candidate_r = curr_r + dr
        #         candidate_c = curr_c + dc

        #         if 0 <= candidate_r < ROWS and 0 <= candidate_c < COLS and grid[candidate_r][candidate_c] == "1":
        #             dfs(candidate_r, candidate_c)

    
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == "1":
        #             dfs(r, c)
        #             res += 1

        def bfs(r, c):
            q = deque()
            q.append((r,c))

            while q:
                curr_r, curr_c = q.popleft()

                for dr, dc in DIRECTIONS:
                    candidate_r = curr_r + dr
                    candidate_c = curr_c + dc

                    if not (0 <= candidate_r < ROWS and 0 <= candidate_c < COLS and grid[candidate_r][candidate_c] == "1"):
                        continue
                    else:
                        q.append((candidate_r, candidate_c))
                        grid[candidate_r][candidate_c] = "0"



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1

                    







        return res
        


        