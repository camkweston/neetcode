from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)
        
        @lru_cache
        def solve(i):
            if i >= N:
                return 0
            else:
                return max(
                    solve(i + 2),
                    solve(i + 3)
                ) + nums[i]
        
        return max(
            solve(0),
            solve(1)
        )


        