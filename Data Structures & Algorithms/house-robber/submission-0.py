class Solution:
    def rob(self, nums: List[int]) -> int:
        last_two = set([len(nums) - 1, len(nums) - 2])

        def solve(n: int, memo: dict) -> int:
            if n >= len(nums):
                return 0
            elif n in last_two:
                return nums[n]
            elif n in memo:
                return memo[n]
            else:
                res = max(
                    solve(n + 2, memo),
                    solve(n + 3, memo)
                ) + nums[n]

                memo[n] = res

                return res
        

        return max(
            solve(0, {}),
            solve(1, {}),
        )
        