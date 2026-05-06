class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        N = len(nums)

        def solve(i: int):
            if i >= N:
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            solve(i + 1)

            subset.pop()
            solve(i + 1)
        

        solve(0)

        return result + []



        