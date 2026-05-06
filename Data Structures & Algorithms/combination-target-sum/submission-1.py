class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []


        def solve(i: int, running_sum:int, curr: list):
            if running_sum == target:
                result.append(curr.copy())
                return
            
            for j in range(i, len(nums)):
                if nums[j] + running_sum > target:
                    return
                else:
                    curr.append(nums[j])
                    solve(j, running_sum + nums[j], curr)
                    curr.pop()


        solve(0, 0, [])

        return result


