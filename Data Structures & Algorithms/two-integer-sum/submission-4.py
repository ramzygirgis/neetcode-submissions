class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i in range(len(nums)):
            complements[target - nums[i]] = i
        keys = complements.keys()
        for j in range(len(nums)):
            if nums[j] in keys:
                if j == complements[nums[j]]:
                    continue
                return [min(complements[nums[j]], j), max(complements[nums[j]], j)]