class Solution:
    def climbStairs(self, k: int) -> int:


        def solve(n: int, memo: dict) -> int:
            if n in memo:
                return memo[n]
            else:
                res = None

                if n <= 2:
                    res = n
                else:
                    res = solve(n-2, memo) + solve(n-1, memo)
                
                memo[n] = res
                
                return res

        

        return solve(k, {})
        