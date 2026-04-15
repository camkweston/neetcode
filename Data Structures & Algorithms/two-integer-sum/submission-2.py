class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            candidate = target - nums[i]
            if candidate in seen:
                return [seen[candidate], i]
            seen[nums[i]] = i
        raise Exception("no match found")
        