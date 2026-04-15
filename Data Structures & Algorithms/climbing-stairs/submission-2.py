class Solution:
    def climbStairs(self, k: int) -> int:


        def solve(n: int, memo: dict) -> int:
            if n in memo:
                return memo[n]
            else:
                res = None

                if n <= 0:
                    res = 0
                elif n == 1:
                    res = 1
                elif n == 2:
                    res = 2
                else:
                    res = solve(n-2, memo) + solve(n-1, memo)
                
                memo[n] = res
                
                return res

        

        return solve(k, {})
        