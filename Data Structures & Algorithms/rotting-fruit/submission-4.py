
DIRECTIONS = [
    (1,0), (0, 1), (-1, 0), (0, -1)
]

from copy import deepcopy

class Solution:
    def simulateOneMinute(self, before: List[List[int]], fresh: set) -> List[List[int]]:
        after = deepcopy(before)

        ROWS = len(before)
        COLS = len(before[0])

        for r in range(ROWS):
            for c in range(COLS):
                if before[r][c] == 1:
                    has_rotten_neighbor = any(
                        before[dr + r][dc + c] == 2
                        for dr,dc in DIRECTIONS
                        if 0 <= dr + r < ROWS and 0 <= dc + c < COLS
                    )
                    print(r,c,has_rotten_neighbor)

                    if has_rotten_neighbor:
                        after[r][c] = 2
                        fresh.remove((r,c))
        
        return after, fresh


        

    def orangesRotting(self, grid: List[List[int]]) -> int:


        # simulate a minute

        # if the grid before == after, break

        # else: simulate another minute

        # if we still have any fresh cells, return -1 else return minutes

        if not grid:
            return 0


        fresh = set()
        minutes = 0

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh.add((r,c))
        

        while True:
            after, fresh = self.simulateOneMinute(grid, fresh)

            if grid == after:
                break
            else:
                minutes += 1
                grid = after
        
        return minutes if len(fresh) == 0 else -1
        











        
        