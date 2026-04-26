

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0 
        elif len(nums) <= 3:
            return max(nums)



        def solve(houses: List[int]) -> int:
            N = len(houses)
            dp = [0] * N
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, N):
                dp[i] = max(
                    dp[i - 1],
                    dp[i - 2] + houses[i]
                )
            
            return dp[N - 1]
        

        skip_last_house = solve(nums[: -1])
        skip_first_house = solve(nums[1: ])

        return max(skip_last_house, skip_first_house)



        

        