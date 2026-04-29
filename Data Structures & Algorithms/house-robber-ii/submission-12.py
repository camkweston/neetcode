class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) <= 3:
            return max(nums)
        


        def helper(houses):
            N = len(houses)
            dp = [0] * N

            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, N):
                dp[i] = max(
                    dp[i-1], dp[i-2] + houses[i]
                )
            
            return dp[-1]
        

        return max(
            helper(nums[ : -1]),
            helper(nums[1 : ])
        )

        