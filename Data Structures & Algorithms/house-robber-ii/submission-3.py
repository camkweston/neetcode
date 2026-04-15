class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        def solve(i: int, started_at_zero: bool, memo: dict) -> int:
            if i >= N or (i == N-1 and started_at_zero):
                return 0
            elif i in memo:
                return memo[i]
            else:
                res = max(
                    solve(i + 1, started_at_zero, memo),
                    nums[i] + solve(i + 2, started_at_zero, memo)
                )

                memo[i] = res

                return res

        
        if N <= 3:
            return max(nums)
        else:
            return max(
                solve(0, True, {}),
                solve(1, False, {})
            )

        