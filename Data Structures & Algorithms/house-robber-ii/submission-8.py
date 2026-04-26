from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)

        if N == 0:
            return 0
        
        if N <= 3:
            return max(nums)
        
        @lru_cache
        def solve(i, did_rob_first_house):
            if i >= N or (i == N - 1 and did_rob_first_house):
                return 0
            else:
                return max(
                    solve(i + 1, did_rob_first_house),
                    solve(i + 2, did_rob_first_house) + nums[i]
                )
        
        return max(
            solve(0, True),
            solve(1, False)
        )



        

        