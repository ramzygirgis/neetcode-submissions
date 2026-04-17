class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[target - nums[i]] = i
        keys = set(d.keys())
        for j in range(len(nums)):
            if nums[j] in keys:
                i = d[nums[j]]
                if i != j:
                    return [min(i, j), max(i, j)]