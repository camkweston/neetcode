class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        N = len(nums)
        
        result = []

        def solve(i: int, curr: list, running_sum: int):
            if running_sum == target:
                result.append(curr.copy())
                return
            
            for j in range(i, N):
                if nums[j] + running_sum > target:
                    return
                curr.append(nums[j])
                solve(j, curr, running_sum + nums[j])
                curr.pop()
        

        solve(0, [], 0)

        return result


