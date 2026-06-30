class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, v in enumerate(nums):
            result = target - v
            if result in seen:
                return [seen[result], i]
            seen[v] = i
