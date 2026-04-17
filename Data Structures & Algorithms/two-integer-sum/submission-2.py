class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            indices[nums[i]] = i
        for i in range(len(nums)):
            if indices.get(target - nums[i]) is not None and indices.get(target - nums[i]) != i:
                return [i, indices[target - nums[i]]]