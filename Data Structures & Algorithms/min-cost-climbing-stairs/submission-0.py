class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)

        def solve(i: int, memo: dict):
            if i >= N:
                return 0
            elif i in memo:
                return memo[i]
            else:
                res = min(
                    solve(i + 2, memo),
                    solve(i + 1, memo)
                ) + cost[i]

                memo[i] = res

                return res
        

        return min(
            solve(0, {}),
            solve(1, {})
        )


        



        