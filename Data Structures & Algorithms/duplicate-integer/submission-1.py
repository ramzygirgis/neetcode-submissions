class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for n in set(nums):
            counts[n] = 0
        for n in nums:
            counts[n] += 1
        for n in set(nums):
            if counts[n] >= 2:
                return True
        return False