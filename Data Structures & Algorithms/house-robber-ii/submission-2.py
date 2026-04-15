class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        def solve(start: int, i: int, memo: dict) -> int:

            if i >= N:
                return 0
            
            if i == N - 1 and start == 0:
                return 0
            

            if i >= N - 2:
                return nums[i]

            if (start, i) in memo:
                return memo[(start, i)]
            
            
            res = max(
                solve(start, i + 2, memo),
                solve(start, i + 3, memo)
            ) + nums[i]


            memo[(start, i)] = res

            return res
        
        if N == 1:
            return nums[0]

        return max(
            solve(0, 0, {}),
            solve(1, 1, {}),
            solve(2, 2, {})
        )

        