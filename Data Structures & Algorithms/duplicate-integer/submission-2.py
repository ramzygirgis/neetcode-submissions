class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for num in nums:
            if counts[num] > 1:
                return True
        return False